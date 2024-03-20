<template>
    <div>
      <button @click="goToAddPage">Add Item</button>
      <table>
        <tr v-for="item in items" :key="item.id">
          <td>{{ item.name }}</td>
          <td>{{ item.description }}</td>
          <td>{{ item.quantity }}</td>
          <td>{{ item.location }}</td>
          <td>
            <button @click="goToEditPage(item.id)">Edit</button>
            <button @click="confirmDelete(item.id)">Delete</button>
          </td>
        </tr>
      </table>
    </div>
  </template>
  
  <script>
  import http from '../http';
  
  export default {
    data() {
      return {
        items: []
      };
    },
    mounted() {
      this.fetchItems();
    },
    methods: {
      fetchItems() {
        http.get('/')
          .then(response => {
            this.items = response.data;
          })
          .catch(error => {
            console.error("There was an error fetching the items: ", error);
          });
      },
      goToEditPage(id) {
        this.$router.push({ name: 'EditItem', params: { id: id } });
      },
      goToAddPage() {
        this.$router.push({ name: 'AddItem' });
      },
      confirmDelete(id) {
        if (confirm("Are you sure you want to delete this item?")) {
            http.delete(`delete/${id}`)
            .then(() => {
              this.fetchItems();
            })
            .catch(error => {
              console.error("There was an error deleting the item: ", error);
            });
        }
      }
    }
  }
  </script>
  