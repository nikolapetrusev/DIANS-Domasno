<template>
  <nav class="navbar">
    <div class="container-fluid px-5">
      <h2>ВиноВодич</h2>
      <div>
        <ul class="nav navbar-nav navbar-right list-group-horizontal gap-5">
          <li class="nav-item"><router-link to="/">Почетна</router-link></li>
          <li class="nav-item"><router-link to="/login">Најава</router-link></li>
          <li class="nav-item"><router-link to="/profile">Профил</router-link></li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "AppHeader"
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
  }

  .router-link-exact-active {
    color: white;
    text-decoration: underline;
  }
</style>