from django.forms import ModelForm
from .models import user_review


class UserReviewForm(ModelForm):
    class Meta:
        model = user_review
        fields = '__all__'
