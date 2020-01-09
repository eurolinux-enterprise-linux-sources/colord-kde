/***************************************************************************
 *   Copyright (C) 2012 by Daniel Nicoletti <dantti12@gmail.com>           *
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 *   This program is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU General Public License     *
 *   along with this program; see the file COPYING. If not, write to       *
 *   the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,  *
 *   Boston, MA 02110-1301, USA.                                           *
 ***************************************************************************/

#include "ProfileNamedColors.h"
#include "ui_ProfileNamedColors.h"

#include <QColor>
#include <QHeaderView>

#include <KDebug>

ProfileNamedColors::ProfileNamedColors(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::ProfileNamedColors)
{
    ui->setupUi(this);

    m_model = new QStandardItemModel(this);
    m_model->setColumnCount(2);
    ui->treeView->setModel(m_model);
    ui->treeView->header()->setResizeMode(0, QHeaderView::ResizeToContents);
}

ProfileNamedColors::~ProfileNamedColors()
{
    delete ui;
}

void ProfileNamedColors::setNamedColors(const QMap<QString, QColor> &namedColors)
{
    m_model->removeRows(0, m_model->rowCount());

    QMap<QString, QColor>::const_iterator i = namedColors.constBegin();
    while (i != namedColors.constEnd()) {
        QList<QStandardItem *> row;
        QStandardItem *name = new QStandardItem(i.key());

        QStandardItem *color = new QStandardItem;
        color->setBackground(QBrush(i.value()));

        row << name;
        row << color;
        m_model->appendRow(row);
        ++i;
    }
}
