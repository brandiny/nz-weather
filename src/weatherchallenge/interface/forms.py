from django import forms

class CityForm(forms.Form):
    CITY_CHOICES = [
        ("auckland", "Auckland"),
        ("christchurch", "Christchurch"),
        ("wellington", "Wellington"),
        ("hamilton", "Hamilton"),
        ("tauranga", "Tauranga"),
        ("napier", "Napier"),
        ("dunedin", "Dunedin")
    ]

    city = forms.CharField(
        label='Choose another city', 
        widget=forms.Select(attrs={"onchange": "this.form.submit()"}, choices=CITY_CHOICES)
    )
    