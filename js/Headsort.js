class Headsort {
  constructor(liste) {
    this.liste = liste;
  }
  gauche(i) {
    return i * 2 + 1;
  }
  droite(i) {
    return i * 2 + 2;
  }
  pere(i) {
    return (i - 1) / 2;
  }

  estTas() {
    for (let i = 0; i < this.liste.lenght - 2; i++) {
      if (this.liste[this.gauche(i)] > this.liste[i]) {
        return false;
      }
      if (
        this.droite(i) < this.liste.lenght &&
        this.liste[this.droite(i)] > this.liste[i]
      ) {
        return false;
      }
    }
    return true;
  }

  maximun(i, lim) {
    let maxi = i;
    const g = this.gauche(i);
    const d = this.droite(i);
    if (g < lim && this.liste[g] > this.liste[maxi]) {
      maxi = g;
    }
    if (d < lim && this.liste[d] > this.liste[maxi]) {
      maxi = d;
    }
    return maxi;
  }
}

module.exports = Headsort;
