<template>
    <div class="">
        <Header></Header>
    </div>
</template>

<script lang="ts">

import Header from './components/Header.vue';
import { defineComponent } from 'vue';
import 'bootstrap/dist/css/bootstrap.css';

export default defineComponent({
    components: {
        Header,
    },
})
</script> 