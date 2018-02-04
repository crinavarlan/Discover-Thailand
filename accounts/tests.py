from .forms import UserRegistrationForm
from django.test import TestCase
from django.conf import settings
from django import forms


class CustomUserTest(TestCase):
    def test_registration_form(self):
        form = UserRegistrationForm({
            'email': 'tester@test.com',
            'password1': 'test123',
            'password2': 'test123',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 9,
            'expiry_year': 2033,
        })
        self.assertTrue(form.is_valid())

    def test_registration_form_fails_with_missing_email(self):
        form = UserRegistrationForm({
            'password1': 'Iwillenter_1',
            'password2': 'Iwillenter_1',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your email address",
                                 form.full_clean())

    def test_registration_fails_with_empty_password1(self):
        form = UserRegistrationForm({
            'email': 'professional_tester@test.com',
            'password2': 'Iwillenter_1',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())

    def test_registration_fails_with_empty_password2(self):
        form = UserRegistrationForm({
            'email': 'professional_tester@test.com',
            'password1': 'Iwillenter_1',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())