<template>
    <div style="display: none;" class="border rounded bg-secondary shadow p-4 mb-4" :id="'messageForm' + productId">
        <p class="h1 mb-4">Send a message</p>
        <form :id="'newMessageForm' + productId" @submit.prevent method="POST">
            <div class="form-group">
                <input class="form-control" type="text" name="text" id="text" placeholder="Enter comment" /><br>
                <input style="display:none" class="form-control" name="productId" id="productId" :placeholder=productId
                    :value=productId /><br>

                <div class="row justify-content-center">
                    <button v-on:click="send_comment()" class="btn btn-light justify-content-center"
                        type="button">Post</button>
                </div>
            </div>
        </form>
    </div>
</template>

<script lang="ts">

import { defineComponent } from 'vue';

type Message = {
    id: number;
    sender: string;
    recipient: string;
    text: string;
    product: number;
    response_id: number;
    time: number
}


export default defineComponent({
    props: ["productId"],


    data() {

        return {
            messages: [] as Message[],
        };
    },

    methods: {

        async send_comment() {
            let messageForm = document.getElementById('newMessageForm' + this.productId) as HTMLFormElement;
            let formData: FormData = new FormData(messageForm)
            let response = await fetch("http://localhost:8000/api/messages", {
                method: "POST",
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",

                body: formData
            });
            let data = await response.json();
            this.$emit('changeMessages', data.messages)
        },
    }
})
</script>