class Procent:
    def countPr(amount, percent):
        a=percent*0.01*amount
        return(a)
    def countSum(amount, percent):
        a = percent * 0.01 * amount+amount
        return (a)
    def countSumTrunc(amount, percent):
        a=round(percent * 0.01 * amount+amount)
        return (a)

class Controller(Procent):

    def countPrNastr(nastr, amount):
        if nastr=="Отличное":
            a=Procent.countPr(amount,15)
        elif nastr=="Нормальное":
            a=Procent.countPr(amount,10)
        elif nastr=="Плохое":
            a=Procent.countPr(amount,3)
        return (a)

    def countSumNastr(nastr, amount):
        if nastr=="Отличное":
            a=Procent.countSum(amount,15)
        elif nastr=="Нормальное":
            a=Procent.countSum(amount,10)
        elif nastr=="Плохое":
            a=Procent.countSum(amount,3)
        return (a)

    def countSumTruncNastr(nastr, amount):
        if nastr=="Отличное":
            a=Procent.countSumTrunc(amount,15)
        elif nastr=="Нормальное":
            a=Procent.countSumTrunc(amount,10)
        elif nastr=="Плохое":
            a=Procent.countSumTrunc(amount,3)
        return (a)


mood=input("Выберите свое настроение: Отлтчное, Хорошее, Плохое\n")
amount=input("Введите сумму чека:\n")

bac=Controller.countPrNastr(str(mood), int(amount))
print("Сумма процентов = "+str(bac))
bac=Controller.countSumNastr(str(mood), int(amount))
print("Итоговая сумма с учетом процентов = "+str(bac))
bac=Controller.countSumTruncNastr(str(mood), int(amount))
print("Итоговая округленная сумма с учетом процентов = "+str(bac))
