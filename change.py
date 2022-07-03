from xml.etree import ElementTree
import csv

# parse
xml = ElementTree.parse("E:\study\steeleye\DLTINS_20210118_01of01.xml")

# create csv
csv = open("data.csv", "w", encoding="utf-8")

# objet to write file
csv_write = csv.write(csv)

# Add header
csv_write.writerow(["Id,FullNm,ClssfctnTp,CmmdtyDerivInd,NtnlCcy"])
for FinInst in xml.findall("FinInstrmGnlAttrbts"):
    if(FinInst):
        id = FinInst.find("Id")
        fname = FinInst.find("FullNm")
        clss = FinInst.find("ClssfctnTp")
        cmm = FinInst.find("CmmdtyDerivInd")
        ntn = FinInst.find("NtnlCcy")

        csvline = [id.text, fname.text, clss.text, cmm.text, ntn.text]
        # push
        csv_write.writer.writerow(csvline)
csv.close()
