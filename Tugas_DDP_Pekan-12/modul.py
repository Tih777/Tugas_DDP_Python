class Gempa:
    lokasi = ''
    skala = ''

    def __init__(self,area,get):
        self.lokasi = area
        self.skala = get

    def gem(self):
        if self.skala <= 2:
            print(self.lokasi,'dengan kekuatan gempa ',self.skala,'skala richter, akan mengakibatkan getaran kecil')

        elif 2 <= self.skala <= 4:
            print(self.lokasi,'dengan kekuatan gempa ',self.skala,'skala richter, akan mengakibatkan bangunan retak-retak')

        elif 4 <= self.skala <=6:
            print(self.lokasi,'dengan kekuatan gempa ',self.skala,'skala richter, akan mengakibatkan bangunan roboh')

        else:
            print(self.lokasi,'dengan kekuatan gempa ',self.skala,'skala richter, akan mengakibatkan potensi tsunami')