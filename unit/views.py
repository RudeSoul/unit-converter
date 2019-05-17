from django.http import HttpResponse
from django.shortcuts import render
from unit.forms import lengthform
from unit.models import length
import operator 

def homepage(request):
	return render(request, 'home.html')

#def lengthview(request):
#	if request_method == 'POST':
#		from = lengthform(request.POST)
#		if form.is_valid():
#			length = request.POST.get('length', '')
#
#			return HttpResponseRedirect(reverse('unit:length'))
#		else:
#			from = lengthform()
#
#		return render(request, 'unit/convert_length.html', { 'form': form, })

 def convert_length(request):
		meter = request.GET['meter']
		i=100
		j=3.28084
		k=39.3701
		centimeter=float(i)*float(meter)
		foot=float(j)*float(meter)
		inch=float(k)*float(meter)
		return render(request, 'convert_length.html',{'centimeter':float(centimeter),'meter' :int(meter), 'foot' :float(foot), 'inch':float(inch), })
def convert_currency(request):
		paisa = request.GET['paisa']
		i=100
		rupee =float(paisa)/float(i)
		return render(request, 'convert_currency.html', {'rupee':float(rupee), 'paisa':float(paisa)})

def convert_power(request):
	value = request.GET['power']
	i=0.284349374
	ans = float(value)*foat(i)
	return render(request, 'convert_power.html', {'ans':float(ans), 'value':float(value)})

def convert_Dynamic_Viscocity(request):
	value = request.GET['value']
	i=0.000671969
	ans = float(value)*float(i)
	return render(request, 'convert_Dynamic_Viscocity.html', {'ans':float(ans), 'value':float(value)})

def convert_heat_flux(request):
	value = request.GET['value']
	i=3.154591
	ans = float(value)*float(i)
	return render(request, 'convert_heat_flux.html', {'ans':float(ans), 'value':float(value)})

def convert_volume(request):
	value = request.GET['value']
	i=3.154591
	ans = float(value)*float(i)
	return render(request, 'convert_volume.html', {'ans':float(ans), 'value':float(value)})

def convert_energy(request):
	value = request.GET['value']
	i=0.000293071
	ans = float(value)*float(i)
	return render(request, 'convert_energy.html', {'ans':float(ans), 'value':float(value)})

def convert_kinematic(request):
	value = request.GET['value']
	i=0.000293071
	ans = float(value)*float(i)
	return render(request, 'convert_kinematic.html', {'ans':float(ans), 'value':float(value)})

def convert_specific(request):
	value = request.GET['value']
	i=0.000293071
	ans = float(value)*float(i)
	return render(request, 'convert_specific.html', {'ans':float(ans), 'value':float(value)})

def convert_molar(request):
	value = request.GET['value']
	i=0.3786675
	ans = float(value)*float(i)
	return render(request, 'convert_molar.html', {'ans':float(ans), 'value':float(value)})

def convert_mass(request):
	value = request.GET['value']
	i=2239.969112
	ans = float(value)*float(i)
	return render(request, 'convert_mass.html', {'ans':float(ans), 'value':float(value)})

def convert_mass_flowrate(request):
	value = request.GET['value']
	i=0.007559873
	ans = float(value)*float(i)
	return render(request, 'convert_mass_flowrate.html', {'ans':float(ans), 'value':float(value)})

def convert_specific_heat(request):
	value = request.GET['value']
	i=4186.8
	ans = float(value)*float(i)
	return render(request, 'convert_specific_heat.html', {'ans':float(ans), 'value':float(value)})

def convert_volumetric_flowrate(request):
	value = request.GET['value']
	i=0.133680546
	ans = float(value)*float(i)
	return render(request, 'convert_volumetric_flowrate.html', {'ans':float(ans), 'value':float(value)})

def convert_density(request):
	value = request.GET['value']
	i=0.01601846
	ans = float(value)*float(i)
	return render(request, 'convert_density.html', {'ans':float(ans), 'value':float(value)})

def convert_area(request):
	value = request.GET['value']
	i=10.76391042
	ans = float(value)*float(i)
	return render(request, 'convert_area.html', {'ans':float(ans), 'value':float(value)})

def convert_pressure(request):
	value = request.GET['value']
	i=51.71508
	ans = float(value)*float(i)
	return render(request, 'convert_pressure.html', {'ans':float(ans), 'value':float(value)})

def convert_Heat_Transfer_Coeffcient(request):
	value = request.GET['value']
	i=0.000567826
	ans = float(value)*float(i)
	return render(request, 'convert_Heat_Transfer_Coeffcient.html', {'ans':float(ans), 'value':float(value)})

def convert_Thermal_Conductivity(request):
	value = request.GET['value']
	i=0.01730735
	ans = float(value)*float(i)
	return render(request, 'convert_Thermal_Conductivity.html', {'ans':float(ans), 'value':float(value)})

