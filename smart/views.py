from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse 
import pandas as pd
import json
from django.http import JsonResponse

def home(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def map(request):
    return render(request, 'map.html')

def profile(request):
   return render(request, 'profile.html')

def admined(request):
    return render(request, 'admined.html')

def data(request):
    return render(request,'data.html')

def details(request):
    return render(request,'details.html')

# def predict(request):
#     return render(request,'predict.html')


def admined_profile(request):
    return render(request, 'admined_profile.html')

# def logout_view(request):
#     request.session.flush()  # Clear session data
#     return redirect('index')  # Redirect to login page
# views.py
import pandas as pd,os
from django.shortcuts import render
from django.conf import settings
from django.http import Http404

from django.conf import settings
import os
import pandas as pd
from django.shortcuts import render

# def predict(request):
#     # Construct the absolute path to the CSV file
#     file_path = os.path.join(settings.BASE_DIR, '.smart_waste_management\newgarbagedata.csv')
    
#     # Debug: Print file path
#     print(f'File path: {file_path}')
    
#     if not os.path.isfile(file_path):
#         return render(request, 'predict.html', {'error': 'File not found'})

#     df = pd.read_csv(file_path)
#     data = df.to_dict(orient='records')
    
#     return render(request, 'predict.html', {'data': data})
import os
from django.conf import settings

def predict(request):
    try:
        # Construct the absolute path to the CSV file
        file_path = os.path.join(settings.BASE_DIR, 'newgarbagedata.csv')
        
        # Debug: Print file path
        print(f'File path: {file_path}')
        
        if not os.path.isfile(file_path):
            return render(request, 'predict.html', {'data': [], 'error': 'File not found'})
        
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Print DataFrame and columns for debugging
        print("DataFrame read from CSV:")
        print(df.head())  # Use head() to print the first few rows

        print("Columns in DataFrame:")
        print(df.columns)
        
        # Remove leading/trailing spaces from column names if any
        df.columns = df.columns.str.strip()

        # Convert DataFrame to a list of dictionaries
        data = df.to_dict(orient='records')
        
        # Print the converted data
        print("Data converted to list of dictionaries:")
        print(data)
        
        # Render template with data
        return render(request, 'predict.html', {'data': data})
    
    except FileNotFoundError:
        print("File not found. Check the file path.")
        return render(request, 'predict.html', {'data': [], 'error': 'File not found'})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'predict.html', {'data': [], 'error': 'An error occurred'})
