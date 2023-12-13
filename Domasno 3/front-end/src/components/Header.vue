<template>
  <nav class="navbar">
    <div class="container-fluid px-5">
      <h2>ВиноВодич</h2>
      <div>
        <ul class="nav navbar-nav navbar-right list-group-horizontal gap-5">
          <li class="nav-item"><router-link to="/">Почетна</router-link></li>
          <li class="nav-item" v-if="userLoggedIn"><a @click="logout">Одјава</a></li>
          <li class="nav-item" v-else><router-link to="/login">Најава</router-link></li>
          <li class="nav-item" v-if="userLoggedIn"><router-link to="/profile">Профил</router-link></li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import router from "@/router";
import {mutations, store} from "@/store/store";

export default {
  name: "AppHeader",
  computed: {
    userLoggedIn() {
      if(store.loggedIn) {
        return store.loggedIn
      }
      else {
        return sessionStorage.getItem("loggedIn") === "true"
      }
    },
  },
  methods: {
    logout() {
      sessionStorage.removeItem('access');
      sessionStorage.removeItem('refresh');
      sessionStorage.setItem('loggedIn', "false");

      mutations.setLoggedIn(false);
      router.push("/")
    }
  }
}
</script>

<style scoped>
  nav {
    background-color: var(--primary-color);
    color: white;
  }

  a {
    text-decoration: none;
    color: white;
    cursor: pointer;
  }

  .router-link-exact-active {
    color: white;
    text-decoration: underline;
  }
</style>