import { reactive } from 'vue';

export const store = reactive({
    selectedCity: null,
    selectedWinery: null,
    selectedRating: 0,
    favoriteClicked: false,
    api_url: "http://127.0.0.1:8000",
    wineries: Array,
    cities: "",
    loggedIn: false,
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
    },
    setWineries(w) {
        store.wineries = w;
    },
    setCities(c) {
        store.cities = c;
    },
    setLoggedIn(value) {
        store.loggedIn = value
    }
};