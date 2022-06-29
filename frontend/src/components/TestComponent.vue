<template>
  <div>
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      axios.get('http://localhost:8000/test')
        .then((res) => {
          this.msg = res.data.name
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>