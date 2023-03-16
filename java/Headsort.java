import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Headsort {
    private List<Integer> liste = new ArrayList<>();

    // Constructor

    public Headsort() {
    }

    public Headsort(List<Integer> liste) {
        this.liste = liste;
    }

    // Methods

    public int gauche(int i) {
        return i * 2 + 1;
    }

    public int droite(int i) {
        return i * 2 + 2;
    }

    public int pere(int i) {
        return (i - 1) / 2;
    }

    public boolean estTas() {
        for (int i = 0; i < (this.liste.size() - 2) / 2; i++) {
            if (this.liste.get(this.gauche(i)) > this.liste.get(i)) {
                return false;
            }
            if (this.droite(i) < this.liste.size() && this.liste.get(this.droite(i)) > this.liste.get(i)) {
                return false;
            }
        }
        return true;
    }

    public Integer maximun(int i, int lim) {
        int maxi = i;
        int g = this.gauche(i);
        int d = this.droite(i);
        if (g < lim && this.liste.get(g) > this.liste.get(maxi)) {
            maxi = g;
        }
        if (d < lim && this.liste.get(d) > this.liste.get(maxi)) {
            maxi = d;
        }
        return maxi;
    }

    public void entasser(int i, int lim) {
        int maxi = this.maximun(i, lim);
        if (maxi != i) {
            int temp = this.liste.get(i);
            this.liste.set(i, this.liste.get(maxi));
            this.liste.set(maxi, temp);
            this.entasser(maxi, lim);
        }
    }

    public void buildheap() {
        ArrayList<Integer> newListe = new ArrayList<>(this.liste);
        Collections.reverse(newListe);
        for (int i = newListe.size() - 1; i >= 0; i--) {
            this.entasser(i, newListe.size());
        }
    }

    public List<Integer> trierParTas() {
        this.buildheap();
        for (int i = liste.size() - 1; i > 0; i--) {
            int temp = this.liste.get(0);
            this.liste.set(0, this.liste.get(i));
            this.liste.set(i, temp);
            this.entasser(0, i);
        }
        return this.liste;
    }
}
