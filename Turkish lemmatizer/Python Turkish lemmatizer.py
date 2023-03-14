import re

class TurkceKelime:
    def __init__(self, kelime):
        self.kelime = kelime
        self.ekler = []
        self.kok = ""

    def ayir(self):
        ekler = []
        kok = self.kelime

        # Çekim eklerini belirleme
        ekler += re.findall(r"(lar|ler|[ae][^aeıioöuü]*[ae]n|[ae][^aeıioöuü]*[ae]m|"
                            r"y[ae][^aeıioöuü]*[ae]m|[^aeıioöuü]*[ae]m|"
                            r"n[ae][^aeıioöuü]*[ae]m|[^aeıioöuü]*[ae]n|"
                            r"[^aeıioöuü]*[ae]n[ıiuü]z|[^aeıioöuü]*[ae]nız|"
                            r"[^aeıioöuü]*[ae]nlar|[^aeıioöuü]*[ae]mız|"
                            r"[^aeıioöuü]*[ae]niz|[^aeıioöuü]*[ae]yla|"
                            r"[^aeıioöuü]*[ae]yle|[^aeıioöuü]*[ae]nda|"
                            r"[^aeıioöuü]*[ae]nde|[ae][^aeıioöuü]*[ae]|" 
                            r"l[ae][^aeıioöuü]*[ae]r|[^aeıioöuü]*[ae]d[eı]|"
                            r"[^aeıioöuü]*[ae]t[ie]|[^aeıioöuü]*[ae]di|"
                            r"[^aeıioöuü]*[ae]t|[^aeıioöuü]*[ae]ti|"
                            r"[^aeıioöuü]*[ae]n[ae]|[ae][^aeıioöuü]*[ae]n|"
                            r"[^aeıioöuü]*[ae]m[ae]|[ae][^aeıioöuü]*[ae]m|"
                            r"[^aeıioöuü]*[ae]da|[^aeıioöuü]*[ae]de|"
                            r"[^aeıioöuü]*[ae]dan|[^aeıioöuü]*[ae]yla|"
                            r"[^aeıioöuü]*[ae]yle|[ae][^aeıioöuü]*[ae]ce|"
                            r"[^aeıioöuü]*[ae]lik|[^aeıioöuü]*[ae]ci|"
                            r"[^aeıio]|")
