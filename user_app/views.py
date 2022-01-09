from django.views.generic import FormView, ListView
from .forms import IndexForm
from .models import AdditionalData


class IndexView(FormView):
    form_class = IndexForm
    template_name = 'user_app/index.html'
    model = AdditionalData
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.model.get_or_none(email=request.POST.get('email'))
        self.is_seen = True
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        if not self.object:
            self.object = form.save()
            self.is_seen = False
        return super().form_invalid(form)  # dirty hack to stay on the same page

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.object:
            data['seen_text'] = self.seen_text
        return data

    @property
    def seen_text(self):
        if self.is_seen:
            return f'Вже бачилися, {self.object.first_name}'
        return f'Привіт, {self.object.first_name} {self.object.last_name}'


class ListOfVisitors(ListView):
    model = AdditionalData
    paginate_by = 20
    ordering = 'first_name'
    template_name = 'user_app/index.html'
    context_object_name = 'visitors'
