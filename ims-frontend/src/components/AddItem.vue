<template>
    <div>
      <form @submit.prevent="addItem">
        <input v-model="item.name" placeholder="Name">
        <input v-model="item.description" placeholder="Description">
        <input v-model="item.quantity" placeholder="Quantity" type="number">
        <input v-model="item.location" placeholder="Location">
        <button type="submit">Submit</button>
      </form>
      <p v-if="errorMessage" style="color: red;">{{ errorMessage }}</p>
    </div>
  </template>
  
  <script>
  import http from '../http';
  
  export default {
    data() {
      return {
        item: {
          name: '',
          description: '',
          quantity: null,
          location: ''
        },
        errorMessage: ''
      };
    },
    methods: {
      addItem() {
        if (!this.item.name || !this.item.description || this.item.quantity === null || !this.item.location) {
          this.errorMessage = 'All fields must be filled.';
          return; 
        }
        this.errorMessage = '';
        
        http.post('/add/', this.item)
          .then(() => {
            this.$router.push({ name: 'Main' });
          })
          .catch(error => {
            console.error("There was an error adding the item: ", error);
            this.errorMessage = 'Failed to add item. Please try again.';
          });
      }
    }
  }
  </script>
  