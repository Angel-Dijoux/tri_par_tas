export class Headsort {
  liste: number[];

  constructor(liste: number[]) {
    this.liste = liste;
  }
  gauche(i: number): number {
    return i * 2 + 1;
  }
  droite(i: number): number {
    return i * 2 + 2;
  }
  pere(i: number): number {
    return (i - 1) / 2;
  }

  estTas(): boolean {
    for (let i = 0; i < this.liste.length - 2; i++) {
      if (this.liste[this.gauche(i)] > this.liste[i]) {
        return false;
      }
      if (
        this.droite(i) < this.liste.length &&
        this.liste[this.droite(i)] > this.liste[i]
      ) {
        return false;
      }
    }
    return true;
  }

  maximun(i: number, lim: number): number {
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
