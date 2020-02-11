from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
    
)
class CheckoutForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '@ username'}))
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    shipping_address = forms.CharField(required=False) #(widget=forms.TextInput(attrs={'placeholder': '1234 Main st.'}))
    shipping_address2 = forms.CharField(required=False) #(required=False, widget=forms.TextInput(attrs={'placeholder': 'apartment or suite.'}))
    shipping_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={'class': 'custom-select d-block w-100'}))
    shipping_zip_code = forms.CharField(required=False) #(widget=forms.TextInput(attrs={'class': 'form-control'}))
    

    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '@ username'}))
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    billing_address = forms.CharField(required=False) #(widget=forms.TextInput(attrs={'placeholder': '1234 Main st.'}))
    billing_address2 = forms.CharField(required=False) #(required=False, widget=forms.TextInput(attrs={'placeholder': 'apartment or suite.'}))
    billing_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={'class': 'custom-select d-block w-100'}))
    billing_zip_code = forms.CharField(required=False) #(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(widget=forms.RadioSelect(), choices=PAYMENT_CHOICES)


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 
    'placeholder': 'Promo code',
    'aria-label': 'Recipient\'s username',
    'aria-describedby': 'basic-addon2'
    }))


class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
    email = forms.EmailField()