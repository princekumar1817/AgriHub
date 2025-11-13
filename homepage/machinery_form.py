# homepage/machinery_form.py
from django import forms
from django.forms import DateInput, Textarea
from .models import Machinery, Machinery_activities, Machinery_maintenance

# Utility to set date widget safely
def set_date_widget_if_present(form_cls, field_name):
    """
    If the form's model has `field_name`, set a HTML5 date input widget for it.
    """
    try:
        if field_name in form_cls.base_fields:
            form_cls.base_fields[field_name].widget = DateInput(attrs={"type": "date"})
    except Exception:
        # safe fallback: ignore if anything goes wrong
        pass

# ========== MachineryForm ==========
class MachineryForm(forms.ModelForm):
    class Meta:
        model = Machinery
        # include all fields to avoid FieldError if we don't know exact model
        fields = "__all__"
        widgets = {
            # fallback widgets if fields exist
            "Purchase_date": DateInput(attrs={"type": "date"}),
            "Operation": Textarea(attrs={"rows": 4}),
        }

# ensure date widget if field name differs
set_date_widget_if_present(MachineryForm, "Purchase_date")
set_date_widget_if_present(MachineryForm, "PurchaseDate")
set_date_widget_if_present(MachineryForm, "purchase_date")


# ========== Machinery_activitiesForm ==========
class Machinery_activitiesForm(forms.ModelForm):
    class Meta:
        model = Machinery_activities
        fields = "__all__"
        widgets = {
            "Activity_date": DateInput(attrs={"type": "date"}),
            "Date": DateInput(attrs={"type": "date"}),
            "Description": Textarea(attrs={"rows": 3}),
        }

# compatibility alias for the misspelled import used in views.py
Machinery_activitesForm = Machinery_activitiesForm

# Set date widgets for common name variants safely
set_date_widget_if_present(Machinery_activitiesForm, "Activity_date")
set_date_widget_if_present(Machinery_activitiesForm, "ActivityDate")
set_date_widget_if_present(Machinery_activitiesForm, "Date")


# ========== Machinery_maintenanceForm ==========
class Machinery_maintenanceForm(forms.ModelForm):
    class Meta:
        model = Machinery_maintenance
        fields = "__all__"
        widgets = {
            "Date": DateInput(attrs={"type": "date"}),
            "Description": Textarea(attrs={"rows": 3}),
        }

set_date_widget_if_present(Machinery_maintenanceForm, "Date")
set_date_widget_if_present(Machinery_maintenanceForm, "Maintenance_date")
