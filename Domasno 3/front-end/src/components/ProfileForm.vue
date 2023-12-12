<template>
  <div class="p-3 py-5">
    <form>
      <div class="d-flex justify-content-between align-items-center mb-3">
        <h4 class="text-right">Подесување на профилот</h4>
      </div>
      <div class="row mt-2">
        <div class="col-md-6">
          <label class="labels">Име</label>
          <input type="text" class="form-control" placeholder="Име" v-model="userInfo.first_name">
        </div>
        <div class="col-md-6">
          <label class="labels">Презиме</label>
          <input type="text" class="form-control" value="" placeholder="Презиме" v-model="userInfo.last_name">
        </div>
      </div>
      <div class="row mt-3">
        <div class="col-md-12">
          <label class="labels">Email</label>
          <input type="text" class="form-control" placeholder="Еmail" value="" v-model="userInfo.email">
        </div>
      </div>
      <div class="row mt-3">
        <div class="col-md-12">
          <label class="labels">Корисничко име</label>
          <input type="text" class="form-control" placeholder="Корисничко име" value="" v-model="userInfo.username">
        </div>
      </div>
      <div class="row mt-3">
        <div class="col-md-6">
          <label class="labels">Стара лозинка</label>
          <input type="text" class="form-control" value="" placeholder="Стара лозинка">
        </div>
        <div class="col-md-6">
          <label class="labels">Нова лозинка</label>
          <input type="text" class="form-control" value="" placeholder="Нова лозинка">
        </div>
      </div>
      <div class="mt-5 text-center"><button class="btn" type="submit" @click="saveInformation">Зачувај</button></div>
    </form>
  </div>
</template>

<script>
export default {
  name: "ProfileForm",
  data() {
    return {
      firstName: "User's first name",
      userInfo: Object,
    }
  },
  mounted() {
    this.fetchUserInfo();
  },
  methods: {
    async fetchUserInfo() {
      const requestOptions = {
        method: "GET",
        headers: {"Content-Type": "application/json", "Authorization": "Bearer " + sessionStorage.getItem("access")},
      };
      const response = await fetch("https://dians-backend.onrender.com/profiles/profile/", requestOptions);
      this.userInfo = await response.json();
      this.userInfo = this.userInfo["user"];
    },
    saveInformation() {
      //TODO implement
    }
  }
}
</script>

<style scoped>
.btn {
  background-color: var(--primary-color);
  color: white;
}

.btn:hover {
  background-color: var(--secondary-color);
  color: var(--primary-color);
  border: 1px solid var(--primary-color);
}
</style>