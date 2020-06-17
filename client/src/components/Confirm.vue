<template>

  <div>
      <h1> {{name}} </h1>
      <span v-for="(itemv,  index) in items" :key="index">
          <p>{{itemv.label}}
            <PlusMinusField v-model="itemv.val" :min="0" :max="10"></PlusMinusField>
          </p>
    </span>
    <br>
    <img  class=AddButton src="../assets/Submit_button.png" height="50px" width="150px" v-on:click="Submit">
  </div>

</template>


<script>
import { EventBus } from '../event-bus.js';
import PlusMinusField from "./PlusMinusField";
import axios from 'axios';

export default {
  name: 'Confirm',
  components: {PlusMinusField},
  props: ['name', 'items'],
  data: function () {
  return {
      values_list: [],
      val: 5,
  }
},
  methods: {
        Submit: function(){
            //let total = 0;
            //for(let i in this.items) total += this.items[i].val || 0;
            //alert(total);
            var itemsArr =  [];
            var i;
            for (i = 0; i < this.items.length; i++) {
                  itemsArr.push({val: this.items[i].val, label: this.items[i].label})
            }

            const path = 'http://localhost:5000/database';
            const sn_obj = {"submitCue": true, "name": this.name, "itemsArr": itemsArr};
               axios.post(path, sn_obj)
                      .then(() => {
                        this.emitFinishSubmitToMain();
                      })
                      .catch((error) => {
                        // eslint-disable-next-line
                        console.error(error);
                        this.emitFinishSubmitToMain();
             });
            
            //alert(total);
        },
        emitFinishSubmitToMain: function() {
          EventBus.$emit('finish-submit', "");
        },
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  color: rebeccapurple;
}
</style>
