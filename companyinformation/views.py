from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Company, Product
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404




class CompanyDetails(ListView):
    model = Company
    template_name = "companyinformation/company_list.html"
    context_object_name = "companies"


class Products(ListView):
    model = Product
    template_name = "companyinformation/product_list.html"
    context_object_name = "products"


class companyInfo(DetailView):
    model = Company
    # template_name = "companyinformation/company_detail.html"
    context_object_name = "companyinfo"
   

class AddNewCompany(CreateView):
    model=Company
    fields=['companyName','Ceo','est_year','origin','logo']
    # template_name="companyinformation/addcompany.html"
    # context_object_name="addnewcompanies"

class editCompany(UpdateView):
    model=Company
    fields=['companyName','Ceo']
    context_object_name="editcompany"

class RemoveCompany(DeleteView):
    model=Company
    context_object_name="removecompany"
    success_url=reverse_lazy('company_list')
   


def emiCalculator(request, pk):
    product = get_object_or_404(Product, pk=pk)

    emi = None
    total_amount = None
    total_interest = None
    loan_amount = ''
    years = ''
    interest_rate = None
    error = ''

    if request.method == 'POST':
        try:
            loan_amount = float(request.POST.get('loan_amount', 0))
            years = int(request.POST.get('years', 0))

            if loan_amount <= 0 or loan_amount >= float(product.price):
                error = 'Loan amount must be greater than 0 and less than product price.'

            elif years not in [1, 2, 5, 10]:
                error = 'Please select a valid loan period.'

            else:
                interest_rate = 11 if years in [1, 2] else 15

                monthly_rate = interest_rate / (12 * 100)
                months = years * 12

                emi = (
                    loan_amount * monthly_rate *
                    (1 + monthly_rate) ** months
                ) / (
                    (1 + monthly_rate) ** months - 1
                )

                total_amount = emi * months
                total_interest = total_amount - loan_amount

        except (ValueError, TypeError):
            error = 'Please enter a valid loan amount and loan period.'

    context = {
        'product': product,
        'emi': emi,
        'total_amount': total_amount,
        'total_interest': total_interest,
        'loan_amount': loan_amount,
        'years': years,
        'interest_rate': interest_rate,
        'error': error,
    }

    return render(request, 'companyinformation/emi_calci.html', context)
