from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def public_book_data(request):    
    return JsonResponse([{       
        'book_name' : 'The Psychology of Money',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/71g2ednj0JL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'Morgan Housel',
    },
    {
        'book_name' : 'Rich Dad Poor Dad',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/81bsw6fnUiL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'Robert Kiyoski',
    },
    {
        'book_name' : 'Atomic Habits',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/91bYsX41DVL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'James Clear',
    },
    {       
        'book_name' : 'The Psychology of Money',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/71g2ednj0JL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'Morgan Housel',
    },
    {
        'book_name' : 'Rich Dad Poor Dad',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/81bsw6fnUiL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'Robert Kiyoski',
    },
    {
        'book_name' : 'Atomic Habits',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/91bYsX41DVL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'James Clear',
    },
    {       
        'book_name' : 'The Psychology of Money',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/71g2ednj0JL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'Morgan Housel',
    },
    {
        'book_name' : 'Rich Dad Poor Dad',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/81bsw6fnUiL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'Robert Kiyoski',
    },
    {
        'book_name' : 'Atomic Habits',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/91bYsX41DVL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'James Clear',
    },
    {       
        'book_name' : 'The Psychology of Money',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/71g2ednj0JL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'Morgan Housel',
    },
    {
        'book_name' : 'Rich Dad Poor Dad',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/81bsw6fnUiL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'Robert Kiyoski',
    },
    {
        'book_name' : 'Atomic Habits',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/91bYsX41DVL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'James Clear',
    },
    {       
        'book_name' : 'The Psychology of Money',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/71g2ednj0JL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'Morgan Housel',
    },
    {
        'book_name' : 'Rich Dad Poor Dad',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/81bsw6fnUiL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'Robert Kiyoski',
    },
    {
        'book_name' : 'Atomic Habits',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/91bYsX41DVL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'James Clear',
    },
    {       
        'book_name' : 'The Psychology of Money',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/71g2ednj0JL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'Morgan Housel',
    },
    {
        'book_name' : 'Rich Dad Poor Dad',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/81bsw6fnUiL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'Robert Kiyoski',
    },
    {
        'book_name' : 'Atomic Habits',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/91bYsX41DVL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'James Clear',
    },
    {       
        'book_name' : 'The Psychology of Money',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/71g2ednj0JL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'Morgan Housel',
    },
    {
        'book_name' : 'Rich Dad Poor Dad',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/81bsw6fnUiL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'Robert Kiyoski',
    },
    {
        'book_name' : 'Atomic Habits',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/91bYsX41DVL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'James Clear',
    },
    {       
        'book_name' : 'The Psychology of Money',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/71g2ednj0JL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'Morgan Housel',
    },
    {
        'book_name' : 'Rich Dad Poor Dad',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/81bsw6fnUiL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'Robert Kiyoski',
    },
    {
        'book_name' : 'Atomic Habits',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/91bYsX41DVL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'James Clear',
    },
    {       
        'book_name' : 'The Psychology of Money',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/71g2ednj0JL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'Morgan Housel',
    },
    {
        'book_name' : 'Rich Dad Poor Dad',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/81bsw6fnUiL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'Robert Kiyoski',
    },
    {
        'book_name' : 'Atomic Habits',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/91bYsX41DVL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'James Clear',
    },
    {       
        'book_name' : 'The Psychology of Money',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/71g2ednj0JL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'Morgan Housel',
    },
    {
        'book_name' : 'Rich Dad Poor Dad',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/81bsw6fnUiL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'Robert Kiyoski',
    },
    {
        'book_name' : 'Atomic Habits',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/91bYsX41DVL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'James Clear',
    },
    {       
        'book_name' : 'The Psychology of Money',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/71g2ednj0JL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'Morgan Housel',
    },
    {
        'book_name' : 'Rich Dad Poor Dad',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/81bsw6fnUiL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'Robert Kiyoski',
    },
    {
        'book_name' : 'Atomic Habits',
        'book_image': 'https://images-eu.ssl-images-amazon.com/images/I/91bYsX41DVL._AC_UL604_SR604,400_.jpg',
        'book_author' : 'James Clear',
    }], safe=False) 

