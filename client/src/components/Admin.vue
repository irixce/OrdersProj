<template>
  <div>
    <b-table striped hover :items="items"></b-table>
  </div>

</template>

<script>
import { EventBus } from '../event-bus.js';

export default {
  name: 'ScreenName',
  props: ['sn'],
  data: function () {
  return {
    items: [
          { age: 40, first_name: 'Dickerson', last_name: 'Macdonald' },
          { age: 21, first_name: 'Larsen', last_name: 'Shaw' },
          { age: 89, first_name: 'Geneva', last_name: 'Wilson' },
          { age: 38, first_name: 'Jami', last_name: 'Carney' }
        ]
  }
},
  methods: {
        mouseIn: function(){
            this.active = !this.active;

        },
        emitDeleteToMain: function() {
          EventBus.$emit('delete-sn', this.sn);
        },
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  color: rebeccapurple;
}

  .ScreenName {
     background: lightskyblue;
     color: darkblue;
     font: bold;
     font-family: Futura;
     font-size: 25px;
      box-shadow: 0px 4px gray;
    border-radius: 5px;
     padding-left: 4px;
     padding-right: 4px;
    display: inline-block; /* change the display type           */
    margin: 10px 10px;

  }

  .ScreenName:hover {
    cursor: pointer;
}

</style>
