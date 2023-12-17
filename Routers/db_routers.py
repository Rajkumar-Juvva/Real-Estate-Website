

class Dbrouters:
    route_app_labels_database = {
        'sale_inventory':'sale_inventory_db',
        'phonebook':'phonebook_db',
        'sale_leads':'sale_leads_db',
        }

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to self.db_name.
        """
        return self.route_app_labels_database.get(model._meta.app_label,None)

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to self.db_name.
        """
        return self.route_app_labels_database.get(model._meta.app_label,None)

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels_database or
            obj2._meta.app_label in self.route_app_labels_database
        ):
           return self.route_app_labels_database[obj1._meta.app_label] == self.route_app_labels_database[obj2._meta.app_label]
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        self.db_name database.
        """
        if app_label in self.route_app_labels_database:
            # print(db == self.route_app_labels_database[app_label],db,app_label,model_name)
            return db == self.route_app_labels_database[app_label]
        return None