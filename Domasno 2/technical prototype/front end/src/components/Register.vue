<template>
  <section>
    <div class="container py-4 h-100">
      <div class="row d-flex justify-content-center align-items-center h-90">
        <div class="col-12 col-md-8 col-lg-6 col-xl-5">
          <div class="card shadow-2-strong" style="border-radius: 1rem;">
            <div class="card-body pad text-center">

              <h3 class="mb-5">Регистрирајте се</h3>
              <form>
                <div class="d-flex justify-content-around gap-3">
                  <div class="form-outline mb-4">
                    <input type="text" class="form-control form-control-lg" placeholder="Име"/>
                  </div>

                  <div class="form-outline mb-4">
                    <input type="text" class="form-control form-control-lg" placeholder="Презиме"/>
                  </div>
                </div>

                <div class="form-outline mb-4">
                  <input type="text" class="form-control form-control-lg" placeholder="Username" required/>
                </div>

                <div class="form-outline mb-4">
                  <input type="password" class="form-control form-control-lg" placeholder="Password" required/>
                </div>

                <div class="form-outline mb-4">
                  <input type="password" class="form-control form-control-lg" placeholder="Password" required/>
                </div>

                <button class="btn btn-lg btn-block" type="submit">Регистрација</button>
              </form>

              <hr class="my-4">
              <div>
                <p class="mb-0">Веќе имате профил? <router-link to="/login">Најавете се!</router-link>
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "RegisterComponent"
}
</script>

<style scoped>
  section{
    background-color: var(--secondary-color);
    height: 91vh;
  }

  .card {
    border-radius: 8px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  }

  h3 {
    color: var(--primary-color);
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

  .pad {
    padding: 2rem!important;
  }

  a {
    color: var(--primary-color);
    text-decoration: underline;
    font-weight: 700;
  }
</style>