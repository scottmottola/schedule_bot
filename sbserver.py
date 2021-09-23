from sbmodels import *
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from datetime import datetime, timedelta


api = Api(app)


user_post_args = reqparse.RequestParser()
user_post_args.add_argument("user_name", type=str, help="User name is required", required=True)
user_post_args.add_argument("user_pass", type=str, help="User pass is required", required=True)

user_update_args = reqparse.RequestParser()
user_update_args.add_argument("search_id", type=int, help="Search ID is required", required=True)
user_update_args.add_argument("user_name", type=str, help="User name is required")
user_update_args.add_argument("user_pass", type=str, help="User pass is required")

user_search_args = reqparse.RequestParser()
user_search_args.add_argument("search_id", type=int, help="Search ID is required")
user_search_args.add_argument("user_name", type=str, help="User name is required")

user_resource_fields = {
    'user_id': fields.Integer,
    'user_name': fields.String,
    'user_pass': fields.String
}


discord_user_post_args = reqparse.RequestParser()
discord_user_post_args.add_argument("user_id", type=int, help="User ID is required", required=True)
discord_user_post_args.add_argument("discord_user_name", type=str, help="Discord user name is required", required=True)

discord_user_update_args = reqparse.RequestParser()
discord_user_update_args.add_argument("search_id", type=int, help="Search ID is required", required=True)
discord_user_update_args.add_argument("user_id", type=int, help="User ID is required")
discord_user_update_args.add_argument("discord_user_name", type=str, help="Discord user name is required")

discord_user_search_args = reqparse.RequestParser()
discord_user_search_args.add_argument("search_id", type=int, help="Search ID is required")
discord_user_search_args.add_argument("discord_user_name", type=str, help="Search ID is required")

discord_user_resource_fields = {
    'discord_user_id': fields.Integer,
    'user_id': fields.Integer,
    'discord_user_name': fields.String
}


discord_server_post_args = reqparse.RequestParser()
discord_server_post_args.add_argument("discord_user_id", type=int, help="Discord user ID is required", required=True)
discord_server_post_args.add_argument("discord_server_name", type=str, help="Discord server name is required", required=True)
discord_server_post_args.add_argument("discord_server_nickname", type=str, help="Discord nickname is required")

discord_server_update_args = reqparse.RequestParser()
discord_server_update_args.add_argument("search_id", type=int, help="Search ID is required", required=True)
discord_server_update_args.add_argument("discord_user_id", type=int, help="Discord user ID is required")
discord_server_update_args.add_argument("discord_server_name", type=str, help="Discord server name is required")
discord_server_update_args.add_argument("discord_server_nickname", type=str, help="Discord nickname is required")

discord_server_search_args = reqparse.RequestParser()
discord_server_search_args.add_argument("search_id", type=int, help="Search ID is required")
discord_server_search_args.add_argument("discord_server_name", type=str, help="Search ID is required")
discord_server_search_args.add_argument("discord_user_id", type=int, help="Search ID is required")

discord_server_resource_fields = {
    'discord_server_id': fields.Integer,
    'discord_user_id': fields.Integer,
    'discord_server_name': fields.String,
    'discord_server_nickname': fields.String
}


discord_channel_post_args = reqparse.RequestParser()
discord_channel_post_args.add_argument("discord_server_id", type=int, help="Discord server ID is required", required=True)
discord_channel_post_args.add_argument("discord_channel_name", type=str, help="Discord channel name is required", required=True)
discord_channel_post_args.add_argument("discord_channel_mute", type=bool, help="Discord mute is required")

discord_channel_update_args = reqparse.RequestParser()
discord_channel_update_args.add_argument("search_id", type=int, help="Search ID is required", required=True)
discord_channel_update_args.add_argument("discord_server_id", type=int, help="Discord server ID is required")
discord_channel_update_args.add_argument("discord_channel_name", type=str, help="Discord channel name is required")
discord_channel_update_args.add_argument("discord_channel_mute", type=bool, help="Discord mute is required")

discord_channel_search_args = reqparse.RequestParser()
discord_channel_search_args.add_argument("search_id", type=int, help="Search ID is required")
discord_channel_search_args.add_argument("discord_channel_name", type=str, help="Search ID is required")

discord_channel_resource_fields = {
    'discord_channel_id': fields.Integer,
    'discord_server_id': fields.Integer,
    'discord_channel_name': fields.String,
    'discord_channel_mute': fields.Boolean
}


planner_post_args = reqparse.RequestParser()
planner_post_args.add_argument("user_id", type=int, help="User ID is required", required=True)
planner_post_args.add_argument("planner_name", type=str, help="Planner name is required", required=True)

planner_update_args = reqparse.RequestParser()
planner_update_args.add_argument("search_id", type=int, help="Search ID is required", required=True)
planner_update_args.add_argument("user_id", type=int, help="User ID is required")
planner_update_args.add_argument("planner_name", type=str, help="Planner name is required")

planner_search_args = reqparse.RequestParser()
planner_search_args.add_argument("search_id", type=int, help="Search ID is required")
planner_search_args.add_argument("planner_name", type=str, help="Search ID is required")
planner_search_args.add_argument("user_id", type=int, help="Search ID is required")

planner_resource_fields = {
    'planner_id': fields.Integer,
    'user_id': fields.Integer,
    'planner_name': fields.String
}


plan_post_args = reqparse.RequestParser()
plan_post_args.add_argument("planner_id", type=int, help="PLanner ID is required", required=True)
plan_post_args.add_argument("plan_name", type=str, help="Plan name is required", required=True)
plan_post_args.add_argument("plan_start", type=str, help="Plan start time/date is required", required=True)
plan_post_args.add_argument("plan_end", type=str, help="Plan end time/date is required", required=True)
plan_post_args.add_argument("repeat", type=bool, help="Repeatable is required")
plan_post_args.add_argument("repeat_frequency", type=str, help="Repeat frequency is required")
plan_post_args.add_argument("repeat_duration", type=str, help="Repeat duration is required")
plan_post_args.add_argument("description", type=str, help="Description is required")

plan_update_args = reqparse.RequestParser()
plan_update_args.add_argument("search_id", type=int, help="Search ID is required", required=True)
plan_update_args.add_argument("planner_id", type=int, help="PLanner ID is required")
plan_update_args.add_argument("plan_name", type=str, help="Plan name is required")
plan_update_args.add_argument("plan_start", type=str, help="Plan start time/date is required")
plan_update_args.add_argument("plan_end", type=str, help="Plan end time/date is required")
plan_update_args.add_argument("repeat", type=bool, help="Repeatable is required")
plan_update_args.add_argument("repeat_frequency", type=str, help="Repeat frequency is required")
plan_update_args.add_argument("repeat_duration", type=str, help="Repeat duration is required")
plan_update_args.add_argument("description", type=str, help="Description is required")

plan_search_args = reqparse.RequestParser()
plan_search_args.add_argument("search_id", type=int, help="Search ID is required")
plan_search_args.add_argument("plan_name", type=str, help="Search ID is required")

plan_resource_fields = {
    'plan_id': fields.Integer,
    'planner_id': fields.Integer,
    'plan_name': fields.String,
    'plan_start': fields.DateTime,
    'plan_end': fields.DateTime,
    'repeat': fields.Boolean,
    'repeat_frequency': fields.DateTime,
    'repeat_duration': fields.DateTime,
    'description': fields.String
}


announcement_post_args = reqparse.RequestParser()
announcement_post_args.add_argument("discord_channel_id", type=int, help="Discord channel ID is required", required=True)
announcement_post_args.add_argument("plan_id", type=int, help="Plan ID is required", required=True)
announcement_post_args.add_argument("announce", type=bool, help="Choosing wether it announces is required", required=True)
announcement_post_args.add_argument("alert", type=str, help="Alert time is required", required=True)

announcement_update_args = reqparse.RequestParser()
announcement_update_args.add_argument("search_id", type=int, help="Search ID is required", required=True)
announcement_update_args.add_argument("discord_channel_id", type=int, help="Discord channel ID is required")
announcement_update_args.add_argument("plan_id", type=int, help="Plan ID is required")
announcement_update_args.add_argument("announce", type=bool, help="Choosing wether it announces is required")
announcement_update_args.add_argument("alert", type=str, help="Alert time is required")

announcement_search_args = reqparse.RequestParser()
announcement_search_args.add_argument("search_id", type=int, help="Search ID is required")
announcement_search_args.add_argument("discord_channel_id", type=int, help="Search ID is required")
announcement_search_args.add_argument("plan_id", type=int, help="Search ID is required")

announcement_resource_fields = {
    'announce_id': fields.Integer,
    'discord_channel_id': fields.Integer,
    'plan_id': fields.Integer,
    'announce': fields.Boolean,
    'alert': fields.DateTime
}


class UsersResource(Resource):
    @marshal_with(user_resource_fields)
    def post(self):
        args = user_post_args.parse_args()
        
        user = Users(user_name=args['user_name'], user_pass=args['user_pass'])

        db.session.add(user)
        db.session.commit()
        print(user)
        return user, 201
    

    @marshal_with(user_resource_fields)
    def get(self):
        args = user_search_args.parse_args()
        result = Users.query.filter((Users.user_id == args['search_id']) | (Users.user_name == args['user_name'])).first()
        if not result:
            abort(404, message="Could not find ID...")
        
        return result
    

    @marshal_with(user_resource_fields)
    def patch(self):
        args = user_update_args.parse_args()
        result = Users.query.filter_by(user_id=args['search_id']).first()
        if not result:
            abort(404, message="Id not found, could not update...")

        if args['user_name']:
            result.user_name = args['user_name']
        if args['user_pass']:
            result.user_pass = args['user_pass']

        db.session.commit()
        return result

    def delete(self):
        args = user_search_args.parse_args()
        result = Users.query.filter_by(user_id=args['search_id']).first()
        if not result:
            abort(404, message="Id not found, could not delete...")
        
        db.session.delete(result)
        db.session.commit()
        return '', 204


class DiscordUserResource(Resource):
    @marshal_with(discord_user_resource_fields)
    def post(self):
        args = discord_user_post_args.parse_args()
        
        discord_user = DiscordUser(user_id=args['user_id'], discord_user_name=args['discord_user_name'])

        db.session.add(discord_user)
        db.session.commit()
        return discord_user, 201
    

    @marshal_with(discord_user_resource_fields)
    def get(self):
        args = discord_user_search_args.parse_args()
        result = DiscordUser.query.filter((DiscordUser.discord_user_id == args['search_id']) | (DiscordUser.discord_user_name == args['discord_user_name'])).first()
        if not result:
            abort(404, message="Could not find ID...")
        
        return result
    

    @marshal_with(discord_user_resource_fields)
    def patch(self):
        args = discord_user_update_args.parse_args()
        result = DiscordUser.query.filter_by(discord_user_id=args['search_id']).first()
        if not result:
            abort(404, message="Id not found, could not update...")

        if args['user_id']:
            result.user_id = args['user_id']
        if args['discord_user_name']:
            result.discord_user_name = args['discord_user_name']

        db.session.commit()
        return result

    def delete(self):
        args = discord_user_search_args.parse_args()
        result = DiscordUser.query.filter_by(discord_user_id=args['search_id']).first()
        if not result:
            abort(404, message="Id not found, could not delete...")
        
        db.session.delete(result)
        db.session.commit()
        return '', 204


class DiscordServerResource(Resource):
    @marshal_with(discord_server_resource_fields)
    def post(self):
        args = discord_server_post_args.parse_args()
        
        discord_server = DiscordServer(discord_user_id=args['discord_user_id'], discord_server_name=args['discord_server_name'], discord_server_nickname=args['discord_server_nickname'])

        db.session.add(discord_server)
        db.session.commit()
        return discord_server, 201
    

    @marshal_with(discord_server_resource_fields)
    def get(self):
        args = discord_server_search_args.parse_args()
        result = DiscordServer.query.all()
        result_list = []
        for servers in result:
            if (servers.discord_server_id == args['search_id']) | (servers.discord_server_name == args['discord_server_name']) | (servers.discord_user_id == args['discord_user_id']):
                result_list.append(servers)
        if not result_list:
            abort(404, message="Could not find ID...")
        
        return result_list
    

    @marshal_with(discord_server_resource_fields)
    def patch(self):
        args = discord_server_update_args.parse_args()
        result = DiscordServer.query.filter_by(discord_server_id=args['search_id']).first()
        if not result:
            abort(404, message="Id not found, could not update...")

        if args['discord_user_id']:
            result.discord_user_id = args['discord_user_id']
        if args['discord_server_name']:
            result.discord_server_name = args['discord_server_name']
        if args['discord_server_nickname']:
            result.discord_server_nickname = args['discord_server_nickname']

        db.session.commit()
        return result

    def delete(self):
        args = discord_server_search_args.parse_args()
        result = DiscordServer.query.filter_by(discord_server_id=args['search_id']).first()
        if not result:
            abort(404, message="Id not found, could not delete...")
        
        db.session.delete(result)
        db.session.commit()
        return '', 204


class DiscordChannelResource(Resource):
    @marshal_with(discord_channel_resource_fields)
    def post(self):
        args = discord_channel_post_args.parse_args()
        
        discord_channel = DiscordChannel(discord_server_id=args['discord_server_id'], discord_channel_name=args['discord_channel_name'], discord_channel_mute=args['discord_channel_mute'])

        db.session.add(discord_channel)
        db.session.commit()
        return discord_channel, 201
    

    @marshal_with(discord_channel_resource_fields)
    def get(self):
        args = discord_channel_search_args.parse_args()
        result = DiscordChannel.query.all()
        result_list = []
        for channels in result:
            if (channels.discord_channel_id == args['search_id']) | (channels.discord_channel_name == args['discord_channel_name']):
                result_list.append(channels)
        if not result_list:
            abort(404, message="Could not find ID...")
        
        return result_list
    

    @marshal_with(discord_channel_resource_fields)
    def patch(self):
        args = discord_channel_update_args.parse_args()
        result = DiscordChannel.query.filter_by(discord_channel_id=args['search_id']).first()
        if not result:
            abort(404, message="Id not found, could not update...")
        
        if args['discord_channel_name']:
            result.discord_channel_name = args['discord_channel_name']
        if args['discord_channel_mute']:
            result.discord_channel_mute = args['discord_channel_mute']

        db.session.commit()
        return result

    def delete(self):
        args = discord_channel_search_args.parse_args()
        result = DiscordChannel.query.filter_by(discord_channel_id=args['search_id']).first()
        if not result:
            abort(404, message="Id not found, could not delete...")
        
        db.session.delete(result)
        db.session.commit()
        return '', 204


class PlannerResource(Resource):
    @marshal_with(planner_resource_fields)
    def post(self):
        args = planner_post_args.parse_args()
        
        planner = Planner(user_id=args['user_id'], planner_name=args['planner_name'])

        db.session.add(planner)
        db.session.commit()
        return planner, 201
    

    @marshal_with(planner_resource_fields)
    def get(self):
        args = planner_search_args.parse_args()
        result = Planner.query.all()
        result_list = []
        for planners in result:
            if (planners.planner_id == args['search_id']) | (planners.planner_name == args['planner_name']) | (planners.user_id == args['user_id']):
                result_list.append(planners)
        if not result_list:
            abort(404, message="Could not find ID...")
        
        return result_list
    

    @marshal_with(planner_resource_fields)
    def patch(self):
        args = planner_update_args.parse_args()
        result = Planner.query.filter_by(planner_id=args['search_id']).first()
        if not result:
            abort(404, message="Id not found, could not update...")
        
        if args['planner_name']:
            result.planner_name = args['planner_name']
        if args['user_id']:
            result.user_id = args['user_id']

        db.session.commit()
        return result

    def delete(self):
        args = planner_search_args.parse_args()
        result = Planner.query.filter_by(planner_id=args['search_id']).first()
        if not result:
            abort(404, message="Id not found, could not delete...")
        
        db.session.delete(result)
        db.session.commit()
        return '', 204


class AnnouncementResource(Resource):
    @marshal_with(announcement_resource_fields)
    def post(self):
        args = announcement_post_args.parse_args()
        
        announcement = Announcement(discord_channel_id=args['discord_channel_id'], plan_id=args['plan_id'], announce=args['announce'], alert=datetime.strptime(args['alert'], '%Y-%m-%dT%H:%M:%S') - timedelta(minutes=10))

        db.session.add(announcement)
        db.session.commit()
        return announcement, 201
    

    @marshal_with(announcement_resource_fields)
    def get(self):
        args = announcement_search_args.parse_args()
        result = Planner.query.all()
        result_list = []
        for announcements in result:
            if (announcements.discord_user_id == args['search_id']) | (announcements.discord_channel_id == args['discord_channel_id']) | ( announcements.plan_id == args['plan_id']):
                result_list.append(announcements)
        if not result_list:
            abort(404, message="Could not find ID...")
        
        return result_list
    

    @marshal_with(announcement_resource_fields)
    def patch(self):
        args = announcement_update_args.parse_args()
        result = Announcement.query.filter_by(announce_id=args['search_id']).first()
        if not result:
            abort(404, message="Id not found, could not update...")
        
        if args['discord_channel_id']:
            result.discord_channel_id = args['discord_channel_id']
        if args['plan_id']:
            result.plan_id = args['plan_id']
        if args['announce']:
            result.announce = args['announce']
        if args['alert']:
            result.alert = args['alert']

        db.session.commit()
        return result

    def delete(self):
        args = announcement_search_args.parse_args()
        result = Announcement.query.filter_by(announce_id=args['search_id']).first()
        if not result:
            abort(404, message="Id not found, could not delete...")
        
        db.session.delete(result)
        db.session.commit()
        return '', 204


class PlanResource(Resource):
    @marshal_with(plan_resource_fields)
    def post(self):
        args = plan_post_args.parse_args()
        
        plan = Plan(planner_id=args['planner_id'], plan_name=args['plan_name'], plan_start=datetime.strptime(args['plan_start'], '%Y-%m-%dT%H:%M:%S'), plan_end=datetime.strptime(args['plan_end'], '%Y-%m-%dT%H:%M:%S'), repeat=args['repeat'], repeat_frequency=datetime.strptime(args['repeat_frequency'], '%Y-%m-%dT%H:%M:%S'), repeat_duration=datetime.strptime(args['repeat_duration'], '%Y-%m-%dT%H:%M:%S'), description=args['description'])

        db.session.add(plan)
        db.session.commit()
        return plan, 201
    

    @marshal_with(plan_resource_fields)
    def get(self):
        args = plan_search_args.parse_args()
        result = Plan.query.all()
        result_list = []
        for plans in result:
            if (plans.plan_id == args['search_id']) | (plans.plan_name == args['plan_name']):
                result_list.append(plans)
        if not result_list:
            abort(404, message="Could not find ID...")
        
        return result_list
    

    @marshal_with(plan_resource_fields)
    def patch(self):
        args = plan_update_args.parse_args()
        result = Plan.query.filter_by(plan_id=args['search_id']).first()
        if not result:
            abort(404, message="Id not found, could not update...")
        
        if args['planner_id']:
            result.planner_id = args['planner_id']
        if args['plan_name']:
            result.plan_name = args['plan_name']
        if args['plan_start']:
            result.plan_start = args['plan_start']
        if args['plan_end']:
            result.plan_end = args['plan_end']
        if args['repeat']:
            result.repeat = args['repeat']
        if args['repeat_frequency']:
            result.repeat_frequency = args['repeat_frequency']
        if args['repeat_duration']:
            result.repeat_duration = args['repeat_duration']
        if args['description']:
            result.description = args['description']

        db.session.commit()
        return result

    def delete(self):
        args = plan_search_args.parse_args()
        result = Plan.query.filter_by(plan_id=args['search_id']).first()
        if not result:
            abort(404, message="Id not found, could not delete...")
        
        db.session.delete(result)
        db.session.commit()
        return '', 204


api.add_resource(UsersResource, "/users")
api.add_resource(DiscordUserResource, "/discorduser")
api.add_resource(DiscordServerResource, "/discordserver")
api.add_resource(DiscordChannelResource, "/discordchannel")
api.add_resource(PlannerResource, "/planner")
api.add_resource(PlanResource, "/plan")
api.add_resource(AnnouncementResource, "/announcement")

if __name__ == "__main__":
    # print(app.url_map)
    app.run(debug=True)


#  