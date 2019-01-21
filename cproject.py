from flask import Flask , render_template , request, redirect, jsonify, url_for , flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Catalog, Item

app = Flask(__name__)

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/catalog.json/')
def catalogsJSON():
    catalogs = session.query(Catalog).all()
    return jsonify(catalogs=[i.serialize for i in catalogs])

@app.route('/catalog/<catalog_name>/json/')
def catalogItemsJSON(catalog_name):
    catalog = session.query(Catalog).filter_by(name = catalog_name).one()
    items = session.query(Item).filter_by(catalog_id = catalog.id).all()
    return jsonify(items=[i.serialize for i in items])

@app.route('/catalog/<catalog_name>/item/<item_name>/json')
def itemJSON(catalog_name, item_name):
    item = session.query(Item).filter_by(name = item_name).one()
    return jsonify(item = item.serialize)

@app.route('/')
@app.route('/catalog/')
def showMain():
    catalogs = session.query(Catalog).order_by(Catalog.name).all()
    return render_template('main.html',catalogs = catalogs)

@app.route('/catalog/new/' ,methods=['GET', 'POST'])
def newCatalog():
    if request.method == 'POST':
        newCatalog = Catalog(name=request.form['name'])
        session.add(newCatalog)
        session.commit()
        flash("new catalog created!")
        return redirect(url_for('showMain'))
    else:    
        return render_template('newCatalog.html')

@app.route('/catalog/<catalog_name>/edit/' , methods=['GET', 'POST'])
def editCatalog(catalog_name):
    fullCatalogName = catalog_name.replace("+"," ")
    catalog = session.query(Catalog).filter_by(name = fullCatalogName).one()
    if request.method == 'POST':
        if request.form['name']:
            catalog.name = request.form['name']
        session.add(catalog)
        session.commit()
        flash("catalog has been edited!")
        return redirect(url_for('showMain'))
    else:
        return render_template('editCatalog.html',catalog = catalog)

@app.route('/catalog/<catalog_name>/delete/' , methods=['GET', 'POST'])
def deleteCatalog(catalog_name):
    fullCatalogName = catalog_name.replace("+"," ")
    catalog = session.query(Catalog).filter_by(name = fullCatalogName).one()
    if request.method == 'POST':
        session.delete(catalog)
        session.commit()
        flash("delete Catalog")
        return redirect(url_for('showMain'))
    else:
        return render_template('deleteCatalog.html',catalog = catalog)

@app.route('/catalog/<catalog_name>/item/')
def showCatalog(catalog_name):
    fullCatalogName = catalog_name.replace("+"," ")
    catalog = session.query(Catalog).filter_by(name = fullCatalogName).one()
    items = session.query(Item).filter_by(catalog_id = catalog.id).all()
    return render_template('showCatalog.html',catalog = catalog, items=items)

@app.route('/catalog/<catalog_name>/item/<item_name>/')
def showItem(catalog_name, item_name):
    fullCatalogName = catalog_name.replace("+"," ")
    fullItemName = item_name.replace("+"," ")
    catalog = session.query(Catalog).filter_by(name = fullCatalogName).one()
    item = session.query(Item).filter_by(name = fullItemName).one()
    return render_template('showItem.html',catalog = catalog, item=item)

@app.route('/catalog/<catalog_name>/item/new/' , methods=['GET', 'POST'])
def newItem(catalog_name):
    fullCatalogName = catalog_name.replace("+"," ")
    catalog = session.query(Catalog).filter_by(name = fullCatalogName).one()
    if request.method == 'POST':
        newItem = Item(name = request.form['name'],description = request.form['description'], catalog_id = catalog.id)
        session.add(newItem)
        session.commit()
        flash("new item created")
        return redirect(url_for('showCatalog', catalog_name=catalog_name))
    else:
        return render_template('newItem.html', catalog=catalog)

@app.route('/catalog/<catalog_name>/item/<item_name>/edit/' , methods=['GET', 'POST'])
def editItem(catalog_name, item_name):
    fullItemName = item_name.replace("+"," ")
    fullCatalogName = catalog_name.replace("+"," ")
    item = session.query(Item).filter_by(name = fullItemName).one()
    catalog = session.query(Catalog).filter_by(name = fullCatalogName).one()
    if request.method == 'POST':
        if request.form['name']:
            item.name = request.form['name']
        if request.form['description']:
            item.description = request.form['description']
        session.add(item)
        session.commit()
        flash("edit Item")
        return redirect(url_for('showItem', catalog_name=catalog_name , item_name=item.name))
    else:
        return render_template('editItem.html', item=item , catalog=catalog)

@app.route('/catalog/<catalog_name>/item/<item_name>/delete/' , methods=['GET', 'POST'])
def deleteItem(catalog_name, item_name):
    fullItemName = item_name.replace("+"," ")
    item = session.query(Item).filter_by(name = fullItemName).one()
    catalog = session.query(Catalog).filter_by(id = item.catalog_id).one()
    if request.method == 'POST':
        session.delete(item)
        session.commit()
        flash("delete Item")
        return redirect(url_for('showCatalog', catalog_name=catalog_name))
    else:
        return render_template('deleteItem.html', item=item , catalog= catalog)

if __name__ == '__main__':
    app.secret_key = 'secret_key'
    app.debug = True
    app.run(host = '0.0.0.0' , port = 8000)