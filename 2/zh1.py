def main():
    def beolvas():
        movies = []
        with open("movies.csv","r",encoding="utf-8") as fin:
            for sor in fin:
                sor = sor.split("\t")
                movies.append({"Cim":sor[0],"Műfaj":sor[1].lower(),"Év":int(sor[-1]),"Studió":sor[2],"Rotten Tomato":int(sor[5])})
        return movies

    def leggyakoribb_mufaj(film_lista):
        mufajL = []
        mufajH = set()
        n = 0
        nums = {}
        out = open("01_kedvenc_mufaj.txt","w",encoding="utf-8")

        for i in film_lista:
            for k in i:
                if k == "Műfaj":
                    mufajL.append(i["Műfaj"].lower())
                    mufajH.add(i["Műfaj"].lower())

        for h in mufajH:
            for l in mufajL:
                if h == l:
                    n += 1
            nums[h] = n
            n = 0

        v = list(nums.values())
        k = list(nums.keys())
        m = k[v.index(max(v))]

        out.write(str(m).upper())

    def legritkabb_mufaj(film_lista):
        mufajL = []
        mufajH = set()
        n = 0
        nums = {}
        # out = open("01.5_nem_kedvenc_mufaj.txt","w",encoding="utf-8")

        for i in film_lista:
            for k in i:
                if k == "Műfaj":
                    mufajL.append(i["Műfaj"].lower())
                    mufajH.add(i["Műfaj"].lower())

        for h in mufajH:
            for l in mufajL:
                if h == l:
                    n += 1
            nums[h] = n
            n = 0

        v = list(nums.values())
        k = list(nums.keys())
        m = k[v.index(min(v))]

        with open("01.5_nem_kedvenc_mufaj.txt","w",encoding="utf-8") as out:
            print(m,file=out)

        # out.write(str(m).upper())

    def legrosszabb_vigjatek(film_lista):
        stuff = []
        out = open("02_legrosszab_vigjatek.txt","w",encoding="utf-8")

        for i in film_lista:
            for k in i:
                if k[1] == "comedy":
                    stuff.append([int(i["Rotten Tomato"]),i["Cim"]])

        print(stuff)

        big = 0
        nev = None
        for i in stuff:
            if i[0] > big:
                big = i[0]
                nev = i[1]

        # out.write(nev)

    def filmeket_torol(film_lista, studio_nev):
        deleted = []
        for i in film_lista:
            for k in i:
                for s in studio_nev:
                    pass


        print(deleted)


    beolvas()
    leggyakoribb_mufaj(beolvas())
    legritkabb_mufaj(beolvas())
    legrosszabb_vigjatek(beolvas())
    filmeket_torol(beolvas(),studio_nev=["Warner Bros","Disney"])

if __name__ == "__main__":
    main()