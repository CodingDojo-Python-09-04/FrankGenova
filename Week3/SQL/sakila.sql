-- 1. What query would you run to get all the customers inside city_id = 312? 
-- Your query should return customer first name, last name, email, and address.

USE sakila;
SELECT customer.first_name, customer.last_name, customer.email, address.address, address.city_id
FROM customer LEFT OUTER JOIN address on customer.address_id = address.address_id
WHERE address.city_id in ('312');

-- 2. What query would you run to get all comedy films? 
-- Your query should return film title, description, release year, rating, special features, and genre (category).

USE sakila;
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name as genre
FROM film 	LEFT OUTER JOIN film_category on film.film_id = film_category.film_id
			LEFT OUTER JOIN category on film_category.category_id = category.category_id;
 
-- 3. What query would you run to get all the films joined by actor_id=5? 
-- Your query should return the actor id, actor name, film title, description, and release year.

USE sakila;
SELECT actor.actor_id, concat(actor.first_name," ",actor.last_name) as actor_name, film.title, film.description, film.release_year
FROM film 	JOIN film_actor on film.film_id = film_actor.film_id
			JOIN actor on film_actor.actor_id = actor.actor_id
WHERE film_actor.actor_id in ('5');

-- 4. What query would you run to get all the customers in store_id = 1 and inside these cities (1, 42, 312 and 459)? 
-- Your query should return customer first name, last name, email, and address.

USE sakila;
SELECT customer.first_name, customer.last_name, customer.email, address.address
FROM customer LEFT OUTER JOIN address on customer.address_id = address.address_id
WHERE address.city_id in ('1', '42', '312', '459');

-- 5. What query would you run to get all the films with a "rating = G" and "special feature = behind the scenes", joined by actor_id = 15? 
-- Your query should return the film title, description, release year, rating, and special feature. 
-- Hint: You may use LIKE function in getting the 'behind the scenes' part.

USE sakila;
SELECT film.title, film.description, film.release_year, film.rating, film.special_features
FROM film 	JOIN film_actor on film.film_id = film_actor.film_id			
WHERE film_actor.actor_id in ('15') AND film.rating in ('G') AND film.special_features like ('%behind%');


-- 6. What query would you run to get all the actors that joined in the film_id = 369? 
-- Your query should return the film_id, title, actor_id, and actor_name.

USE sakila;
SELECT film.film_id, film.title, film_actor.actor_id, concat(actor.first_name," ", actor.last_name) as actor_name
FROM film 	LEFT OUTER JOIN film_actor on film.film_id = film_actor.film_id
			LEFT OUTER JOIN actor on film_actor.actor_id = actor.actor_id
WHERE film.film_id in ('369');            

-- 7. What query would you run to get all drama films with a rental rate of 2.99? 
-- Your query should return film title, description, release year, rating, special features, and genre (category).

USE sakila;
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name as genre
FROM film LEFT OUTER JOIN film_category on film.film_id = film_category.film_id
			LEFT OUTER JOIN category on film_category.category_id = category.category_id
WHERE film.rental_rate in ('2.99') AND category.name like ('Drama');

-- 8. What query would you run to get all the action films which are joined by SANDRA KILMER? 
-- Your query should return film title, description, release year, rating, special features, genre (category), and actor's first name and last name.

USE sakila;
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name as genre, actor.first_name, actor.last_name
FROM film 	LEFT OUTER JOIN film_category on film.film_id = film_category.film_id
			LEFT OUTER JOIN category on film_category.category_id = category.category_id
            LEFT OUTER JOIN film_actor on film.film_id = film_actor.film_id
			LEFT OUTER JOIN actor on film_actor.actor_id = actor.actor_id
WHERE category.name in ('Action') AND actor.first_name in ('SANDRA') and actor.last_name in ('KILMER');

