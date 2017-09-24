SELECT
	f_users.first_name
    ,f_users.last_name
    ,f_friends.first_name as friend_first_name
    ,f_friends.last_name AS friend_last_name

FROM 
	friendships	LEFT JOIN users AS f_users		ON friendships.user_id 		= f_users.id
				LEFT JOIN users AS f_friends 	ON friendships.friend_id	= f_friends.id 
                
ORDER BY
	f_friends.last_name
    ;
    