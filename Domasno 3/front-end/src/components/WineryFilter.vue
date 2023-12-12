<template>
  <div class="filters col-md-3 p-2">
    <div class="top d-flex justify-content-around align-items-center">
      <form @submit="selectRating">
        <div class="ratingFilter d-flex align-items-center">
          <div class="field">
            <label for="rating">Филтрирај според оцена</label>
            <input type="text" v-model="rating" id="rating" class="form-control-sm" placeholder="Внесете оцена"/>
          </div>
          <button type="submit" class="btn btn-block btn-sm">Примени</button>
        </div>
      </form>
      <button type="submit" class="btn" @click="clearRating">✖</button>
    </div>
    <div class="bottom">
      <div class="cityFilter d-flex align-items-center">
        <h6>Филтрирај според град</h6>
        <button type="submit" class="btn" @click="clearCity">✖</button>
      </div>
      <div class="scrollbar">
        <div v-for="city in allCities" :key="city">
          <button type="submit" class="btn btn-link" @click="selectCity(city)">{{ city }}</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mutations } from '../store/store.js'
export default {
  name: "WineryFilter",
  data() {
    return {
      cities: Array,
      rating: null,
    }
  },
  props: {
    wineries: Object,
  },
  computed: {
    allCities() {
      const cities = new Set();
      if(Array.isArray(this.wineries)) {
        this.wineries.forEach(winery => cities.add(winery.city.name));
      }
      return Array.from(cities);
    },
  },
  // mounted() {
  //   this.fetchCities();
  // },
  methods: {
    // async fetchCities() {
    //   const response = await fetch("https://dians-backend.onrender.com/wineries");
    //   this.wineries = await response.json();
    //   this.wineries = JSON.parse(JSON.stringify(this.wineries))["wineries"]
    //   this.allCities()
    // },
    // TODO proveri dali se vnesuva pravilna vrednost za rejtingot (0-5)
    selectCity(city) {
      mutations.setSelectedCity(city);
    },
    selectRating() {
      mutations.setSelectedRating(this.rating);
    },
    clearRating() {
      this.rating = null
      mutations.setSelectedRating(0);
    },
    clearCity() {
      mutations.setSelectedCity(0)
    }
  }
}
</script>

<style scoped>
  .field {
    display: flex;
    flex-direction: column;
  }

  .cityFilter {
    gap: 53%;
  }

  .top {
    gap: 16%;
  }

  label {
    font-weight: 500;
    line-height: 1.2;
  }

  .bottom {
    border-top: 1px solid black;
    margin-top: .5rem;
    padding-top: .5rem;
  }

  .top, .bottom {
    width: 100%;
    overflow: hidden;
  }

  .btn {
    color: var(--secondary-color);
  }

  .btn-link {
    color: black;
    text-decoration: none;
  }

  .btn-link:hover {
    color: var(--primary-color);
  }

  .btn-sm {
    height: 10%;
    margin-left: .5rem;
    background-color: var(--primary-color);
    color: white;
  }

  .btn-sm:hover {
    background-color: var(--secondary-color);
    border: 1px solid var(--primary-color);
    color: var(--primary-color);
  }

  .form-control-sm {
    border: 1px solid lightgrey;
  }

  .scrollbar {
    height: 63vh;
    overflow-y: scroll;
    overflow-x: hidden;
  }

  .scrollbar::-webkit-scrollbar {
    width: .8rem;
  }

  .scrollbar::-webkit-scrollbar-track {
    border-radius: 8px;
    background-color: var(--secondary-color);
    border: 1px solid #cacaca;
    box-shadow: inset 0 0 6px rgba(0, 0, 0, .3);
  }

  .scrollbar::-webkit-scrollbar-thumb {
    border-radius: 8px;
    background-color: var(--primary-color);
  }

  @media only screen and (max-width: 1200px) {
    .ratingFilter {
      flex-direction: column;
      align-items: center;
    }
  }
</style>