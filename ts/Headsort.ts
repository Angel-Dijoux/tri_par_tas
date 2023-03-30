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
  entasser(i: number, lim: number) {
    let maxi = this.maximun(i, lim);
    if (maxi != i) {
      let tmp = this.liste[i];
      this.liste[i] = this.liste[maxi];
      this.liste[maxi] = tmp;
      this.entasser(maxi, lim);
    }
  }

  builHeap() {
    const newListe: number[] = this.liste;
    newListe.reverse();
    for (let i = this.liste.length - 1; i >= 0; i--) {
      this.entasser(i, newListe.length);
    }
  }

  trierParTas(): number[] {
    this.builHeap();
    for (let i = this.liste.length - 1; i > 0; i--) {
      let tmp = this.liste[0];
      this.liste[0] = this.liste[i];
      this.liste[i] = tmp;
      this.entasser(0, i);
    }
    return this.liste;
  }
}
