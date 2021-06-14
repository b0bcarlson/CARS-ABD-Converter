import csv

@authenticate
def carstoabd(request):
	source = request.FILES.getlist("csv")[0]

	with open(settings.CSV_DIR + "abd.csv", "w") as result:
		writer = csv.writer(result)
		for line in source:
			line = line.decode()
			lst = line.split(",")
			try:
				writer.writerow((lst[3], "0", lst[2]))
			except IndexError:
				pass
	return redirect(settings.CSV_PATH + "abd.csv")
