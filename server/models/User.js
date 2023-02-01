const Sequelize = require('sequelize');

module.exports = class User extends Sequelize.Model {
    static init(sequelize){
        return super.init({
            uid : {
                type: Sequelize.STRING(50),
                allowNull: false,
                unique: true
            },
            password : {
                type: Sequelize.STRING(50),
                allowNull: false
            }
        })
    }
}