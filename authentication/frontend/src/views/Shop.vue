<!-- <template>
    <div>Route Test</div>
    
</template>  -->
<template>

    <div class="container">

        <!-- <Header></Header> -->
        <input class="form-control me-sm-2" type="text" v-model="searchTerm" placeholder="Search product..">
        <!-- <button class="btn btn-secondary my-2 my-sm-0" type="submit">Filter items</button> -->

        <h1 class="">Items On Sale</h1>
        <button @click="showProductPostForm()">List New Product</button>

        <div style="display: none;" class="border rounded bg-secondary shadow p-4 mb-4" id="newProduct">
            <p class="h1 mb-4">Enter a new item</p>
            <form id="newProductForm" @submit.prevent method="POST">
                <div class="form-group">
                    <input class="form-control" type="text" name="title" id="title"
                        placeholder="Enter item's title" /><br>
                    <input class="form-control" type="text" name="description" id="description"
                        placeholder="Write a description" /><br><br>
                    <input class="form-control" type="number" name="starting_price" id="starting_price"
                        placeholder="Enter starting price" /><br>
                    <input class="form-control" type="date" name="finish_date" id="finish_date"
                        placeholder="Enter finish date" /><br>
                    <input class="form-control-image" type="file" name="picture" id="picture"
                        accept="image/png, image/jpeg, image/jpg" placeholder="Upload image" /><br>

                    <div class="row justify-content-center">
                        <button v-on:click="send_product()"
                            class="btn btn-primary btn-lg d-flex justify-content-center mt-3"
                            type="button">Create</button>
                    </div>
                </div>
            </form>
        </div>


        <ul class="list-group">
            <div v-for="product in filteredItems" :id="'product' + product.id" :key="product.id">
                <li class=" list-group-item border border-3 border-primary mb-3" v-if="product.active">
                    <div class="product">
                        <div class="left-sec">

                            <p class="display-5 border rounded border-4"><strong>{{ product.title }}</strong></p>
                            <p class="h5">Description: {{ product.description }}</p>
                            <p class="h5">By: {{ product.owner }}</p>

                            <p class="h5"><img class="prodPics" :src="'http://localhost:8000' + product.picture" /></p>
                            <div v-if="!product.bid_on">
                                <p class="h5">Starting price: {{ product.starting_price }}</p>
                                <p class="h5">No bids</p>
                            </div>
                            <div v-if="product.bid_on">
                                <p class="h5">Highest Bid: {{ product.starting_price }}</p>
                                <p class="h5"> {{ product.highest_bidder }}</p>
                            </div>
                            <p class="h5">Finish date: {{ product.finish_date }}</p>
                        </div>
                        <div class="right-sec">
                            <!-- Bid form -- to be introduced -->
                            <button class="btn btn-primary" @click="showBidForm(product.id)">Bid</button>
                            <Bid @changeProducts="changeProds($event)" :price=product.starting_price :pid=product.id>
                            </Bid>

                            <div class="card bg-light mb-3">
                                <div class="card-header">Comments</div>
                                <div class="card-body">
                                    <div v-for="message in messages">
                                        <div class="fw-lighter pb-2 mb-1 h5 card-title"
                                            v-if="(message.product == product.id)">
                                            <div style="display: flex; align-items: center; gap: 1em; flex-wrap: wrap;">
                                                <p style="color: red;">@{{ message.sender }}</p>
                                                <p>{{ message.text }}</p>

                                            </div>
                                            <div v-for="resp in responses">
                                                <div v-if="(resp.id == message.response_id)">
                                                    <div class="card-text " v-if="resp.text != 'Default'">
                                                        <div
                                                            style="display: flex; align-items: center; gap: 1em; flex-wrap: wrap;">
                                                            <p style="color: blue;">@{{ product.owner }}</p>
                                                            <p>{{ resp.text }}</p>

                                                        </div>

                                                    </div>
                                                </div>
                                            </div>
                                            <div v-if="product.owner == username">
                                                <button class="btn" @click="showReplyForm(message.id)">Reply</button>
                                                <AddResponse :messageId=message.id
                                                    @changeResponses="changeResponses($event)" style="display: none;">
                                                </AddResponse>

                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <button class="btn btn-dark" @click="showMessageForm(product.id)">Message</button>
                                <AddMessage :productId=product.id @changeMessages="changeMessages($event)"></AddMessage>
                            </div>
                        </div>
                    </div>
                </li>

            </div>
        </ul>


    </div>


</template>

<script lang="ts">

import Header from '../components/Header.vue';
import NewItem from '../components/NewItem.vue';
import AddMessage from '../components/AddMessage.vue';
import AddResponse from '../components/AddResponse.vue';

import Bid from '../components/Bid.vue';

import { defineComponent } from 'vue';

import 'bootstrap/dist/css/bootstrap.css';

type Product = {
    id: number;
    active: boolean;
    title: string;
    description: string;
    picture: string;
    starting_price: number;
    highest_bidder: string;
    owner: string;
    finish_date: number;
    bid_on: boolean;
}

type Message = {
    id: number;
    sender: string;
    text: string;
    product: number;
    response_id: number;
    time: number
}

type Response = {
    id: number;
    text: string;
}


type Profile = {
    id: number,
    email: string;
    date_of_birth: Date;
    profile_picture: string;
}

export default defineComponent({
    mounted() {
        this.get_profile_details();
        this.fetch_products();
        this.fetch_messages();
        this.fetch_responses();



    },

    components: {
        NewItem,
        // Header,
        AddMessage,
        Bid,
        AddResponse,
    },


    data() {

        return {
            products: [] as Product[],
            messages: [] as Message[],
            responses: [] as Response[],
            profile: {} as Profile,
            username: '',
            searchTerm: '',
        };
    },

    computed: {
        filteredItems() {
            return this.products.filter(product => product.title.toLowerCase().includes(this.searchTerm.toLowerCase()));
        }
    },

    methods: {
        showProductPostForm() {
            let form1 = document.getElementById('newProduct') as HTMLElement;
            if (form1.style.display == 'none') {
                form1.style.display = 'block'
            }
            else {
                form1.style.display = 'none'
            }
        },
        showMessageForm(prodId: number) {
            let form1 = document.getElementById('messageForm' + prodId) as HTMLElement;
            if (form1.style.display == 'none') {
                form1.style.display = 'block'
            }
            else {
                form1.style.display = 'none'
            }
        },
        showBidForm(prodId: number) {
            let form1 = document.getElementById('bidForm' + prodId) as HTMLElement;
            if (form1.style.display == 'none') {
                form1.style.display = 'block'
            }
            else {
                form1.style.display = 'none'
            }
        },
        showReplyForm(messageId: number) {
            let form1 = document.getElementById('replyForm' + messageId) as HTMLElement;
            if (form1.style.display == 'none') {
                form1.style.display = 'block'
            }
            else {
                form1.style.display = 'none'
            }
        },

        async get_profile_details() {
            let response = await fetch("http://localhost:8000/api/profile", {
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
            });
            if (response.ok) {
                let data = await response.json();
                if (data.logged_in == false) {
                    window.location.href = 'http://localhost:8000/login/';
                }
                this.username = data.username;
                this.profile = data.profile;
            }
            else {
                alert("Connection lost...")
            }
        },


        async changeResponses(responses: []) {
            this.responses = responses
            this.messages = this.messages
            this.products = this.products
            console.log('thisis', this.responses)
        },

        async changeMessages(messages: []) {
            this.messages = messages
        },
        async changeProds(products: []) {
            this.products = products
        },
        async send_product() {
            let productForm = document.getElementById('newProductForm') as HTMLFormElement;
            let formData: FormData = new FormData(productForm)
            let date = document.getElementById('finish_date') as HTMLFormElement;
            var today = new Date();
            let response = await fetch("http://localhost:8000/api/products", {
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
                method: "POST",
                body: formData
            });
            let data = await response.json();
            console.log(data)
            this.products = data.products;
            productForm.reset()

        },

        async fetch_products() {

            let response = await fetch("http://localhost:8000/api/products", {
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
            });
            if (response.ok) {
                let data = await response.json();
                this.products = data.products;

            }
            else {
                alert("Connection lost...")
            }
        },

        async fetch_messages() {

            let response = await fetch("http://localhost:8000/api/messages", {
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
            });
            if (response.ok) {
                let data = await response.json();
                this.messages = data.messages;
            }
            else {
                alert("Connection lost...")
            }
        },
        async fetch_responses() {

            let response = await fetch("http://localhost:8000/api/responses", {
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
            });
            if (response.ok) {
                let data = await response.json();
                this.responses = data.responses;
            }
            else {
                alert("Connection lost...")
            }
        },
    }
})
</script> 