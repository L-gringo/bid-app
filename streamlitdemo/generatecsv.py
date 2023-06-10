import csv

def gencsv(csvname,datas,fieldnames):

    try:
        with open (csvname, "w") as csvfile:
            writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(datas)

    except Exception as error:
        print("le chemin du fichier indiqué ne semble pas correct; essayez en doublant chaque Slash de votre chemin")
        raise error



