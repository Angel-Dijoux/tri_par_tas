"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Headsort = void 0;
var Headsort = /** @class */ (function () {
    function Headsort(liste) {
        this.liste = liste;
    }
    Headsort.prototype.gauche = function (i) {
        return i * 2 + 1;
    };
    Headsort.prototype.droite = function (i) {
        return i * 2 + 2;
    };
    Headsort.prototype.pere = function (i) {
        return (i - 1) / 2;
    };
    Headsort.prototype.estTas = function () {
        for (var i = 0; i < this.liste.length - 2; i++) {
            if (this.liste[this.gauche(i)] > this.liste[i]) {
                return false;
            }
            if (this.droite(i) < this.liste.length &&
                this.liste[this.droite(i)] > this.liste[i]) {
                return false;
            }
        }
        return true;
    };
    Headsort.prototype.maximun = function (i, lim) {
        var maxi = i;
        var g = this.gauche(i);
        var d = this.droite(i);
        if (g < lim && this.liste[g] > this.liste[maxi]) {
            maxi = g;
        }
        if (d < lim && this.liste[d] > this.liste[maxi]) {
            maxi = d;
        }
        return maxi;
    };
    Headsort.prototype.entasser = function (i, lim) {
        var maxi = this.maximun(i, lim);
        if (maxi != i) {
            var tmp = this.liste[i];
            this.liste[i] = this.liste[maxi];
            this.liste[maxi] = tmp;
            this.entasser(maxi, lim);
        }
    };
    Headsort.prototype.builHeap = function () {
        var newListe = this.liste;
        newListe.reverse();
        for (var i = this.liste.length - 1; i >= 0; i--) {
            this.entasser(i, newListe.length);
        }
    };
    Headsort.prototype.trierParTas = function () {
        this.builHeap();
        for (var i = this.liste.length - 1; i > 0; i--) {
            var tmp = this.liste[0];
            this.liste[0] = this.liste[i];
            this.liste[i] = tmp;
            this.entasser(0, i);
        }
        return this.liste;
    };
    return Headsort;
}());
exports.Headsort = Headsort;
