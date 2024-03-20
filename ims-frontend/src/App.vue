<script setup>
import '@/assets/base.css';
import '@/assets/custom.css';
</script>

<template>
   <main>
      <router-view/>
    </main>
</template>

<style scoped>
/* Base styling */
body, html {
  margin: 0;
  padding: 0;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: #f4f7f6;
  color: #333;
}

header {
  background-color: #6200ea; /* Rich purple header */
  color: #fff;
  padding: 1rem 0;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1); /* Soft shadow for depth */
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  text-align: center;
  margin-bottom: 2rem;
  color: #ffffff;
}

/* Using Flexbox for layout */
@media (min-width: 1024px) {
  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 2rem;
  }

  .logo {
    margin: 0;
    font-size: 2rem; /* Larger logo on wider screens */
  }

  .navigation {
    display: flex;
    gap: 1rem; /* Evenly spaced navigation items */
  }

  .navigation a {
    text-decoration: none;
    color: #ffffff;
    background-color: #7b1fa2; /* Slightly darker purple for contrast */
    padding: 0.5rem 1rem;
    border-radius: 4px;
    transition: background-color 0.3s ease; /* Smooth background color transition */
  }

  .navigation a:hover {
    background-color: #9c27b0; /* Lighter purple on hover */
  }
}
</style>

