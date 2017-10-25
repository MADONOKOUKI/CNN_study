str = "";
elems = document.getElementsByClassName('rg_ic rg_i');
for (i = 0; i < elems.length; i++){ str += elems[i].src + '\n'; }
document.write(str);
