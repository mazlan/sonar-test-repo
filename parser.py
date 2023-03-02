# This is a sample Python script.
import csv

fake_secret = "asddfilhpaf78h78032h780g780fg780asg780dsbovncubuyvqy"

def parse_csv_to_xml(csv_file='final.csv'):
    f = open(csv_file)
    csv_f = csv.reader(f)
    for row in csv_f:
        #print(convert_row(row)+'\n')
        print(convert_row_with_classifier(row)+'\n')
    f.close()


def convert_row(row):
    return """<dependency>
    <groupId>%s</groupId>
    <artifactId>%s</artifactId>
    <version>%s</version>
</dependency>""" % (
        row[0], row[1], row[2])


def convert_row_with_classifier(row):
    return """<dependency>
    <groupId>%s</groupId>
    <artifactId>%s</artifactId>
    <version>%s</version>
    <classifier>client</classifier>
</dependency>""" % (
        row[0], row[1], row[2])


if __name__ == '__main__':
    parse_csv_to_xml()


