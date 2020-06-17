<template>

  <div>
  <div v-show="showMain">
    <h1>Enter name:</h1>
    <div class="MainPage">
      <input class="InputBox" v-model="full_name" placeholder="" >
    </div>
    <br>
    <img  class=OKButton src="../assets/OK_button_2.png" height="50px" width="150" v-on:click="ClickOK()">
  </div>

    <Confirm v-bind:name="full_name" v-bind:items="items" v-if="showConfirm"/>

  </div>


</template>


<script>
  import axios from 'axios';
  import Confirm from "./Confirm";
  import { EventBus } from '../event-bus.js';


  export default {
  name: 'Main',
  data() {
    return {
      full_name: '',
      items: [],
      showMain: true,
      showConfirm: false
    }
  },
  methods: {
    getItems() {
      const path = 'http://localhost:5000/items';
      axios.get(path)
              .then((res) => {
                var itemsArr =  [];
                var i;
                for (i = 0; i < res.data.items.length; i++) {
                  itemsArr.push({val: 0, label: res.data.items[i]})
                }
                this.items = itemsArr;
              })
              .catch((error) => {
                // eslint-disable-next-line
                console.error(error);
              });
    },
    ClickOK() {
      if (this.full_name == "") {
        alert("Must enter a name to order.")
      } else {
        this.getItems();
        this.showConfirm = true;
        this.showMain = false;
      }

    },
  },
  components: {
    Confirm
  },
  created() {
    EventBus.$on('finish-submit', name => {
        this.showConfirm = false;
        this.showMain = true;
        this.full_name = name;
  });

  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

   .MainPage {
    display: inline-block;
    vertical-align: middle;
     padding-bottom: 50px;
}
  .InputBox  {
    border-radius: 0px;
    border-color: #11557C;
    border-top: none;
    border-left: none;
    border-right: none;
    border-bottom-width: thick;
    font-size: 25px;
    padding-right: 20px;
    padding-left: 20px;
    font-family: Monaco;
    vertical-align: top;
  }

  .OKButton:hover{
    cursor:pointer;
  }


</style>
