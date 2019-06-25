def rand25() {
 return 5*rand5() + rand5();
}
def method1() {
  int r = Integer.MAX_INT;
  while (r > 6) r = rand25()/3;
  return r;
}

def method2(){

    do{
    row=rand5()
    col=rand5()
    idx=col+(row-1)*7
    }while(idx>40)
    return 1+idx%10
    }
