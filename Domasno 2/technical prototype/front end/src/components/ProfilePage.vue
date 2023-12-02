<template>
  <div class="container rounded bg-white mt-4">
    <div class="row">
      <div class="col-md-3 border-right">
        <div class="d-flex flex-column align-items-center text-center py-5"><img class="rounded-circle mt-5" :src="userIcon"><span class="font-weight-bold">wine_enthusiast1</span><span class="text-black-50">wine_enthusiast1@mail.com</span><span> </span></div>
      </div>
      <div class="col-md-5 border-right">
        <div class="p-3 py-5">
          <div class="d-flex justify-content-between align-items-center mb-3">
            <h4 class="text-right">Подесување на профилот</h4>
          </div>
          <div class="row mt-2">
            <div class="col-md-6"><label class="labels">Име</label><input type="text" class="form-control" placeholder="Име" value=""></div>
            <div class="col-md-6"><label class="labels">Презиме</label><input type="text" class="form-control" value="" placeholder="Презиме"></div>
          </div>
          <div class="row mt-3">
            <div class="col-md-12"><label class="labels">Email</label><input type="text" class="form-control" placeholder="Еmail" value=""></div>
          </div>
          <div class="row mt-3">
            <div class="col-md-12"><label class="labels">Корисничко име</label><input type="text" class="form-control" placeholder="Корисничко име" value=""></div>
          </div>
          <div class="row mt-3">
            <div class="col-md-6"><label class="labels">Стара лозинка</label><input type="text" class="form-control" value="" placeholder="Стара лозинка"></div>
            <div class="col-md-6"><label class="labels">Нова лозинка</label><input type="text" class="form-control" value="" placeholder="Нова лозинка"></div>
          </div>
          <div class="mt-5 text-center"><button class="btn" type="button">Зачувај</button></div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="comments p-3 py-5">
          <div class="d-flex justify-content-between align-items-center experience pb-3">
            <h5>Мои коментари</h5>
          </div>
          <div class="scrollbar">
            <ProfileComment username="wine_enthusiast1" comment="Visited a fantastic winery last weekend. The vineyard views were breathtaking, and the wine tasting experience was unparalleled!" rating="5"></ProfileComment>
            <ProfileComment username="wine_enthusiast1" comment="The winery staff was incredibly knowledgeable. I learned so much about different grape varieties and the winemaking process." rating="4.5"></ProfileComment>
            <ProfileComment username="wine_enthusiast1" comment="The winery staff was incredibly knowledgeable. I learned so much about different grape varieties and the winemaking process." rating="4.5"></ProfileComment>
            <ProfileComment username="wine_enthusiast1" comment="The winery staff was incredibly knowledgeable. I learned so much about different grape varieties and the winemaking process." rating="4.5"></ProfileComment>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import userimg from '../assets/userimg.png';
import ProfileComment from "@/components/ProfileComment";
export default {
  name: "ProfilePage",
  components: {ProfileComment},
  data() {
    return {
      userIcon: userimg
    }
  }
}
</script>

<style scoped>
  .container {
    margin-right: 2rem;
    margin-left: 2rem;
  }

  .row {
    margin-top: 2rem;
  }

  .col-md-3, .col-md-5 {
    background-color: var(--secondary-color);
    border-radius: 8px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    margin-bottom: 2.2rem;
  }

  .col-md-3 {
    border-bottom-right-radius: 0;
    border-top-right-radius: 0;
  }

  .col-md-5 {
    border-bottom-left-radius: 0;
    border-top-left-radius: 0;
  }

  img {
    width: 10rem;
  }

  .btn {
    background-color: var(--primary-color);
    color: white;
  }

  .btn:hover {
    background-color: white;
    color: var(--primary-color);
    border: 1px solid var(--primary-color);
  }

  .labels {
    font-size: 11px
  }

  .comments {
    background-color: var(--secondary-color);
    border-radius: 8px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    margin-left: 3rem;
    width: 31rem;
    height: 33rem;
  }

  .scrollbar {
    height: 100%;
    overflow-y: scroll;
    overflow-x: hidden;
    padding-right: .5rem;
  }

  .scrollbar::-webkit-scrollbar {
    width: 12px;
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
</style>