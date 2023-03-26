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
    return Headsort;
}());
exports.Headsort = Headsort;
