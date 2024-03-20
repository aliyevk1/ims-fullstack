<template>
    <div>
      <form @submit.prevent="updateItem">
        <input v-model="item.name" placeholder="Name">
        <input v-model="item.description" placeholder="Description">
        <input v-model="item.quantity" type="number" placeholder="Quantity">
        <input v-model="item.location" placeholder="Location">
        <button type="submit">Update</button>
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
          id: this.$route.params.id,
          name: '',
          description: '',
          quantity: null,
          location: ''
        },
        errorMessage: '' // Holds the error message
      };
    },
    mounted() {
      this.fetchItem();
    },
    methods: {
      fetchItem() {
        http.get(`/${this.item.id}`)
          .then(response => {
            this.item = response.data;
          })
          .catch(error => {
            console.error("There was an error fetching the item: ", error);
            this.errorMessage = 'Failed to fetch item. Please try again.';
          });
      },
      updateItem() {
        if (!this.item.name || !this.item.description || this.item.quantity === null || !this.item.location) {
          this.errorMessage = 'All fields must be filled.';
          return; 
        }
  
        this.errorMessage = '';
  
        http.put(`edit/${this.item.id}`, this.item)
          .then(() => {
            this.$router.push({ name: 'Main' });
          })
          .catch(error => {
            console.error("There was an error updating the item: ", error);
            this.errorMessage = 'Failed to update item. Please try again.';
          });
      }
    }
  }
  </script>
  