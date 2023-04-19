# Generated by Django 4.1.7 on 2023-04-18 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GoodsInfo",
            fields=[
                (
                    "g_id",
                    models.CharField(
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=8,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "g_brand",
                    models.CharField(
                        blank=True,
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=16,
                        null=True,
                    ),
                ),
                (
                    "g_class",
                    models.CharField(
                        blank=True,
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=16,
                        null=True,
                    ),
                ),
                (
                    "g_name",
                    models.CharField(
                        blank=True,
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=16,
                        null=True,
                    ),
                ),
                ("g_life", models.DateTimeField(blank=True, null=True)),
                (
                    "g_loc",
                    models.TextField(
                        blank=True, db_collation="Chinese_PRC_CI_AS", null=True
                    ),
                ),
                (
                    "g_vendor",
                    models.CharField(
                        blank=True,
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=16,
                        null=True,
                    ),
                ),
                ("g_tempreture", models.FloatField(blank=True, null=True)),
                ("g_humidity", models.FloatField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "货物信息",
                "verbose_name_plural": "货物信息",
                "db_table": "goods_info",
            },
        ),
        migrations.CreateModel(
            name="StaffInfo",
            fields=[
                (
                    "s_id",
                    models.CharField(
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=8,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "s_name",
                    models.CharField(
                        blank=True,
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=16,
                        null=True,
                    ),
                ),
                ("s_salary", models.BigIntegerField(blank=True, null=True)),
                ("s_onboarddate", models.DateTimeField(blank=True, null=True)),
                (
                    "s_gender",
                    models.CharField(
                        blank=True,
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=4,
                        null=True,
                    ),
                ),
                ("s_birth", models.DateTimeField(blank=True, null=True)),
                (
                    "s_department",
                    models.CharField(
                        blank=True,
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=16,
                        null=True,
                    ),
                ),
                (
                    "s_job",
                    models.TextField(
                        blank=True, db_collation="Chinese_PRC_CI_AS", null=True
                    ),
                ),
            ],
            options={
                "verbose_name": "员工信息",
                "verbose_name_plural": "员工信息",
                "db_table": "staff_info",
            },
        ),
        migrations.CreateModel(
            name="TransferInfo",
            fields=[
                (
                    "transfer_id",
                    models.CharField(
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=8,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("transfer_amount", models.BigIntegerField(blank=True, null=True)),
                (
                    "transfer_inaccount",
                    models.CharField(
                        blank=True,
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=19,
                        null=True,
                    ),
                ),
                (
                    "transfer_outaccount",
                    models.CharField(
                        blank=True,
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=19,
                        null=True,
                    ),
                ),
                (
                    "transfer_class",
                    models.CharField(
                        blank=True,
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=4,
                        null=True,
                    ),
                ),
                (
                    "transfer_staffid",
                    models.CharField(
                        blank=True,
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=8,
                        null=True,
                    ),
                ),
                (
                    "transfer_staffname",
                    models.CharField(
                        blank=True,
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=16,
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "转账信息",
                "verbose_name_plural": "转账信息",
                "db_table": "transfer_info",
            },
        ),
        migrations.CreateModel(
            name="TransportationInfo",
            fields=[
                (
                    "transportation_id",
                    models.CharField(
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=8,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "transportation_class",
                    models.TextField(
                        blank=True, db_collation="Chinese_PRC_CI_AS", null=True
                    ),
                ),
                (
                    "driver_name",
                    models.CharField(
                        blank=True,
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=16,
                        null=True,
                    ),
                ),
                (
                    "driver_id",
                    models.CharField(
                        blank=True,
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=8,
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "车辆信息",
                "verbose_name_plural": "车辆信息",
                "db_table": "transportation_info",
            },
        ),
        migrations.CreateModel(
            name="WarehouseInfo",
            fields=[
                (
                    "wh_id",
                    models.CharField(
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=8,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "wh_loc",
                    models.CharField(
                        blank=True,
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=16,
                        null=True,
                    ),
                ),
                (
                    "wh_chief",
                    models.CharField(
                        blank=True,
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=16,
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "仓库信息",
                "verbose_name_plural": "仓库信息",
                "db_table": "warehouse_info",
            },
        ),
        migrations.CreateModel(
            name="TransportRecord",
            fields=[
                (
                    "transport_id",
                    models.CharField(
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=8,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "transport_to",
                    models.CharField(
                        blank=True,
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=16,
                        null=True,
                    ),
                ),
                (
                    "transport_predicatedtime",
                    models.DateTimeField(blank=True, null=True),
                ),
                ("transport_realtime", models.DateTimeField(blank=True, null=True)),
                (
                    "transportation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fresh.transportationinfo",
                    ),
                ),
                (
                    "wh",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fresh.warehouseinfo",
                    ),
                ),
            ],
            options={
                "verbose_name": "运输记录",
                "verbose_name_plural": "运输记录",
                "db_table": "transport_record",
            },
        ),
        migrations.CreateModel(
            name="OutboundRecord",
            fields=[
                (
                    "out_id",
                    models.CharField(
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=8,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("out_time", models.DateTimeField(blank=True, null=True)),
                (
                    "g",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fresh.goodsinfo",
                    ),
                ),
                (
                    "wh",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fresh.warehouseinfo",
                    ),
                ),
            ],
            options={
                "verbose_name": "出库记录",
                "verbose_name_plural": "出库记录",
                "db_table": "outbound_record",
            },
        ),
        migrations.CreateModel(
            name="OrderInfo",
            fields=[
                (
                    "order_id",
                    models.CharField(
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=8,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("order_time", models.DateTimeField(blank=True, null=True)),
                ("order_quantity", models.SmallIntegerField(blank=True, null=True)),
                ("order_realprice", models.BigIntegerField(blank=True, null=True)),
                (
                    "client_name",
                    models.CharField(
                        blank=True,
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=16,
                        null=True,
                    ),
                ),
                (
                    "client_addr",
                    models.CharField(
                        blank=True,
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=16,
                        null=True,
                    ),
                ),
                (
                    "client_tel",
                    models.CharField(
                        blank=True,
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=11,
                        null=True,
                    ),
                ),
                (
                    "g",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fresh.goodsinfo",
                    ),
                ),
                (
                    "out",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fresh.outboundrecord",
                    ),
                ),
                (
                    "transfer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fresh.transferinfo",
                    ),
                ),
                (
                    "transport",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fresh.transportrecord",
                    ),
                ),
            ],
            options={
                "verbose_name": "订单信息",
                "verbose_name_plural": "订单信息",
                "db_table": "order_info",
            },
        ),
        migrations.CreateModel(
            name="KpiInfo",
            fields=[
                ("k_ym", models.DateTimeField(primary_key=True, serialize=False)),
                ("kpi", models.FloatField(blank=True, null=True)),
                ("realsalary", models.BigIntegerField(blank=True, null=True)),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="更新时间"),
                ),
                (
                    "s",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fresh.staffinfo",
                    ),
                ),
            ],
            options={
                "verbose_name": "员工绩效信息",
                "verbose_name_plural": "员工绩效信息",
                "db_table": "KPI_info",
            },
        ),
        migrations.CreateModel(
            name="StockInfo",
            fields=[
                (
                    "wh",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="fresh.warehouseinfo",
                    ),
                ),
                ("s_quantity", models.SmallIntegerField(blank=True, null=True)),
                (
                    "g",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fresh.goodsinfo",
                    ),
                ),
            ],
            options={
                "verbose_name": "库存信息",
                "verbose_name_plural": "库存信息",
                "db_table": "stock_info",
                "unique_together": {("wh", "g")},
            },
        ),
        migrations.CreateModel(
            name="CountRecord",
            fields=[
                (
                    "g",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="fresh.goodsinfo",
                    ),
                ),
                ("count_date", models.DateTimeField(blank=True, null=True)),
                (
                    "count_match",
                    models.CharField(
                        blank=True,
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=4,
                        null=True,
                    ),
                ),
                ("count_quantity", models.SmallIntegerField(blank=True, null=True)),
                (
                    "wh",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fresh.warehouseinfo",
                    ),
                ),
            ],
            options={
                "verbose_name": "盘点记录",
                "verbose_name_plural": "盘点记录",
                "db_table": "count_record",
                "unique_together": {("g", "wh")},
            },
        ),
        migrations.CreateModel(
            name="BuyRecord",
            fields=[
                (
                    "g",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="fresh.goodsinfo",
                    ),
                ),
                (
                    "buy_id",
                    models.CharField(
                        blank=True,
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=8,
                        null=True,
                    ),
                ),
                ("buy_quantity", models.SmallIntegerField(blank=True, null=True)),
                ("buy_intime", models.DateTimeField(blank=True, null=True)),
                ("buy_pdate", models.DateTimeField(blank=True, null=True)),
                ("buy_price", models.BigIntegerField(blank=True, null=True)),
                (
                    "buy_valid",
                    models.CharField(
                        blank=True,
                        db_collation="Chinese_PRC_CI_AS",
                        max_length=4,
                        null=True,
                    ),
                ),
                (
                    "return_reason",
                    models.TextField(
                        blank=True, db_collation="Chinese_PRC_CI_AS", null=True
                    ),
                ),
                (
                    "wh",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fresh.warehouseinfo",
                    ),
                ),
            ],
            options={
                "verbose_name": "采购记录",
                "verbose_name_plural": "采购记录",
                "db_table": "buy_record",
                "unique_together": {("g", "wh")},
            },
        ),
    ]
