import { reactive } from 'vue';

export const store = reactive({
    selectedCity: null,
    selectedWinery: null,
    selectedRating: 0,
    favoriteClicked: false,
});

export const mutations = {
    setSelectedCity(city) {
        store.selectedCity = city;
    },
    setSelectedWinery(winery) {
        store.selectedWinery = winery;
    },
    setSelectedRating(rating) {
        store.selectedRating = rating;
    },
    toggleFavorite() {
        store.favoriteClicked = !store.favoriteClicked
    }
};