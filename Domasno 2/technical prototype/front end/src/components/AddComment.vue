<template>
  <div class="card">
    <div class="row">
      <div class="col-10">
        <div class="comment-box ml-2">
          <h4>Додајте коментар и оцена</h4>
          <div class="rating">
            <input type="radio" name="rating" value="5" id="5"><label for="5">☆</label>
            <input type="radio" name="rating" value="4" id="4"><label for="4">☆</label>
            <input type="radio" name="rating" value="3" id="3"><label for="3">☆</label>
            <input type="radio" name="rating" value="2" id="2"><label for="2">☆</label>
            <input type="radio" name="rating" value="1" id="1"><label for="1">☆</label>
          </div>
          <div class="comment-area">
            <textarea class="form-control" placeholder="Додајте коментар..." rows="4"></textarea>
          </div>
          <div class="comment-btns mt-2">
            <div class="row">
              <div class="col-6">
                <button class="btn btn-success send btn-sm">Зачувај<i class="fa fa-long-arrow-right ml-1"></i></button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AddComment"
}
</script>

<style scoped>
  .card {
    background-color: var(--secondary-color);
    padding: 1rem;
    width:95%;
    background-clip: border-box;
    border-radius: 8px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  }

  .comment-box{
    padding: 1rem 3rem;
  }

  .comment-area textarea{
    width: 100%;
    resize: none;
    border: 1px solid #ad9f9f;
  }


  .form-control:focus {
    color: #495057;
    box-shadow: 0 0 0 1px var(--primary-color) !important;
  }

  .send {
    color: #fff;
    background-color: var(--primary-color);
    border-color: var(--primary-color);
  }

  .send:hover {
    color: #fff;
    background-color: var(--primary-color);
    border-color: var(--primary-color);
  }

  .rating {
    display: flex;
    margin-top: -10px;
    flex-direction: row-reverse;
    margin-left: -4px;
    float: left;
  }

  .rating>input {
    display: none
  }

  .rating>label {
    position: relative;
    width: 19px;
    font-size: 25px;
    color: var(--primary-color);
    cursor: pointer;
  }

  .rating>label::before {
    content: "\2605";
    position: absolute;
    opacity: 0
  }

  .rating>label:hover:before,
  .rating>label:hover~label:before {
    opacity: 1 !important
  }

  .rating>input:checked~label:before {
    opacity: 1
  }

  .rating:hover>input:checked~label:before {
    opacity: 0.4
  }
</style>